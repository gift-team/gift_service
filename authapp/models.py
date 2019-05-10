from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField
# from addressapp.models import Address


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class GiftUser(AbstractUser):
    objects = UserManager()

    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    MALE = 'M'
    FEMALE = 'W'

    GENDER_CHOICE = (
        (MALE, 'Мужчина'),
        (FEMALE, 'Женщина')
    )

    middle_name = models.CharField(verbose_name='отчество', max_length=150, blank=True)
    address = models.ManyToManyField('Address', related_name='address', blank=True)
    avatar = models.ImageField(upload_to='client_avatars', blank=True)
    age = models.PositiveIntegerField(verbose_name='возраст', blank=True, null=True)
    email = models.EmailField(verbose_name='почта', unique=True)
    phone = PhoneNumberField(verbose_name='телефон', unique=True, blank=True, null=True)
    gender = models.CharField(verbose_name='пол', max_length=1, choices=GENDER_CHOICE, blank=True)

    active_key = models.CharField(max_length=128, verbose_name='код подтверждения', blank=True)
    active_key_expires = models.DateTimeField(default=timezone.now() + timezone.timedelta(48))

    def is_activation_key_expired(self):
        if timezone.now() <= self.active_key_expires:
            return False
        else:
            return True


# TODO Убрать после тестирования переопределение метода __str__. Красоту наводят на фронте
class AddressName(models.Model):
    name = models.CharField(verbose_name='название адреса', max_length=20, unique=True, null=False, blank=False)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(verbose_name='название страны', max_length=30, unique=True, null=False, blank=False)

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(verbose_name='область', max_length=30, unique=True, null=False, blank=False)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(verbose_name='населенный пункт', max_length=30, unique=True, null=False, blank=False)

    def __str__(self):
        return self.name


class Street(models.Model):
    name = models.CharField(verbose_name='улица', max_length=30, unique=True, null=False, blank=False)

    def __str__(self):
        return self.name


class Building(models.Model):
    number = models.IntegerField(verbose_name='дом', unique=False, null=False, blank=False)
    structure = models.CharField(verbose_name='к., стр., вл.', max_length=3, unique=False, null=True, blank=True)

    def __str__(self):
        return '{}{}{}'.format(self.number, '-', self.structure)


class Flat(models.Model):
    number = models.IntegerField(verbose_name='квартира', unique=True, null=False, blank=False)

    def __str__(self):
        return '%s' % self.number


class Addresses(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    street = models.ForeignKey(Street, on_delete=models.CASCADE)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    flat = models.ForeignKey(Flat, on_delete=models.CASCADE)
    str_name = models.CharField(max_length=500, blank=True)

    def save(self, force_insert=False, force_update=False):
        self.str_name = self.country.__str__() + self.region.__str__() + \
                        self.city.__str__() + self.street.__str__() + \
                        self.building.__str__() + self.flat.__str__()
        super(Addresses, self).save(force_insert, force_update)

    def __str__(self):
        result = str(self.country) + ', '+ str(self.region) + ', ' + \
        str(self.city) + ', ' + str(self.street) + ', ' + \
        str(self.building) + ', ' + str(self.flat)
        return result


class Address(models.Model):
    user = models.ForeignKey(GiftUser,
                             related_name='users',
                             verbose_name='владелец',
                             unique=False,
                             null=False,
                             blank=False,
                             on_delete=models.CASCADE)
    name = models.ForeignKey(AddressName, on_delete=models.CASCADE)
    addresses = models.ForeignKey(Addresses, on_delete=models.CASCADE, related_name='addresses')

    def __str__(self):
        return 'Владелец: {}, адрес: {}. {}, {}, {}, {}, {}-{}'.format(self.user.get_full_name(),
                                                                       self.name,
                                                                       self.addresses.country,
                                                                       self.addresses.region,
                                                                       self.addresses.city,
                                                                       self.addresses.street,
                                                                       self.addresses.building,
                                                                       self.addresses.flat)
