from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class AddressName(models.Model):
    name = models.CharField(verbose_name='название адреса', max_length=20, unique=True, null=False, blank=False)


class Country(models.Model):
    name = models.CharField(verbose_name='название страны', max_length=30, unique=True, null=False, blank=False)


class Region(models.Model):
    name = models.CharField(verbose_name='область', max_length=30, unique=True, null=False, blank=False)


class City(models.Model):
    name = models.CharField(verbose_name='населенный пункт', max_length=30, unique=True, null=False, blank=False)


class Street(models.Model):
    name = models.CharField(verbose_name='улица', max_length=30, unique=True, null=False, blank=False)


class Building(models.Model):
    number = models.IntegerField(verbose_name='дом', unique=False, null=False, blank=False)
    structure = models.CharField(verbose_name='к., стр., вл.', max_length=3, unique=False, null=True, blank=True)


class Address(models.Model):
    user = models.ForeignKey('authapp.GiftUser', related_name='+', on_delete=models.CASCADE)
    name = models.ForeignKey(AddressName, on_delete=models.SET(1))
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    street = models.ForeignKey(Street, on_delete=models.CASCADE)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
