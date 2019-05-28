from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField


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

    country = models.CharField(verbose_name='название страны', max_length=30, null=True, blank=True)
    region = models.CharField(verbose_name='область', max_length=30, null=True, blank=True)
    city = models.CharField(verbose_name='населенный пункт', max_length=30,  null=True, blank=True)
    street = models.CharField(verbose_name='улица', max_length=30,  null=True, blank=True)
    building = models.CharField(verbose_name='дом', max_length=7,  null=True, blank=True)
    flat = models.IntegerField(verbose_name='квартира',  null=True, blank=True)

    login = models.CharField(verbose_name='логин', max_length=20, blank=True, null=True)
    avatar = models.ImageField(upload_to='client_avatars', blank=True, null=True)
    birthdate = models.DateField(verbose_name='дата рождения', blank=True, null=True)
    email = models.EmailField(verbose_name='почта', unique=True)
    phone = PhoneNumberField(verbose_name='телефон', blank=True, null=True)
    gender = models.CharField(verbose_name='пол', max_length=1, choices=GENDER_CHOICE, blank=True)

    active_key = models.CharField(max_length=128, verbose_name='код подтверждения', blank=True)
    active_key_expires = models.DateTimeField(default=timezone.now() + timezone.timedelta(48))

    def is_activation_key_expired(self):
        if timezone.now() <= self.active_key_expires:
            return False
        else:
            return True


class AddressList(models.Model):
    name = models.CharField(verbose_name='название адреса', max_length=20, null=False, blank=False)
    country = models.CharField(verbose_name='название страны', max_length=30, unique=False,  null=False, blank=False)
    region = models.CharField(verbose_name='область', max_length=30, unique=False,  null=False, blank=False)
    city = models.CharField(verbose_name='населенный пункт', max_length=30, unique=False,  null=False, blank=False)
    street = models.CharField(verbose_name='улица', max_length=30, unique=False,  null=False, blank=False)
    building = models.CharField(verbose_name='дом', max_length=7, unique=False, null=False, blank=False)
    flat = models.IntegerField(verbose_name='квартира', unique=False, null=False, blank=False)

    def __str__(self):
        result = str(self.country) + ', '+ str(self.region) + ', ' + \
        str(self.city) + ', ' + str(self.street) + ', ' + \
        str(self.building) + ', ' + str(self.flat)
        return result
