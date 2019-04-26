from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from address.models import AddressField


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
    address = AddressField(related_name='+', on_delete=models.CASCADE, blank=True, null=True)
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


# class AddressName(models.Model):
#     name = models.CharField(verbose_name='название адреса', max_length=20, unique=True, null=False, blank=False)
#
#
# class Address(models.Model):
#     user_id = models.ForeignKey(GiftUser, on_delete=models.CASCADE)
#     name_id = models.ForeignKey(AddressName, on_delete=models.SET(1))
#     address = AddressField(related_name='+', blank=True, null=True)


# Моя пиздобратия до того, как увидел, что ты уже добавил django-address
# class AddressName(models.Model):
#     name = models.CharField(verbose_name='название адреса', max_length=20, unique=True, null=False, blank=False)
#
#
# class Country(models.Model):
#     name = models.CharField(verbose_name='название страны', max_length=30, unique=True, null=False, blank=False)
#
#
# class Region(models.Model):
#     country_id = models.ForeignKey(Country, on_delete=models.CASCADE)
#     name = models.CharField(verbose_name='область', max_length=20, unique=True, null=False, blank=False)
#
#
# class City(models.Model):
#     region_id = models.ForeignKey(Region, on_delete=models.CASCADE)
#     name = models.CharField(verbose_name='населенный пункт', max_length=20, unique=True, null=False, blank=False)
#
#
# class Street(models.Model):
#     city_id = models.ForeignKey(City, on_delete=models.CASCADE)
#     name = models.CharField(verbose_name='улица', max_length=20, unique=True, null=False, blank=False)
#
#
# class Building(models.Model):
#     street_id = models.ForeignKey(Street, on_delete=models.CASCADE)
#     number = models.IntegerField(verbose_name='дом', max_length=6, unique=True, null=False, blank=False)
#
#
# class BuildingStructure(models.Model):
#     building_id = models.ForeignKey(Building, on_delete=models.CASCADE)
#     name = models.IntegerField(verbose_name='дом', max_length=6, unique=True, null=False, blank=False)
#
#
# class Address(models.Model):
#     user_id = models.ForeignKey(GiftUser, on_delete=models.CASCADE)
#     name_id = models.ForeignKey(AddressName, on_delete=models.SET(1))
#     country_id =
