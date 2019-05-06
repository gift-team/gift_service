from django.db import models

# Create your models here.


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


class Address(models.Model):
    user = models.IntegerField(verbose_name='владелец', unique=False, null=False, blank=False)
    name = models.ForeignKey(AddressName, on_delete=models.SET(1))
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    street = models.ForeignKey(Street, on_delete=models.CASCADE)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)


    def __str__(self):
        return 'ID владелеца: {}, адрес: {}. {}, {}, {}, {}, {}'.format(self.user,
                                                                        self.name,
                                                                        self.country,
                                                                        self.region,
                                                                        self.city,
                                                                        self.street,
                                                                        self.building)


