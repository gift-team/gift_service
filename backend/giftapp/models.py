from django.db import models
from authapp.models import GiftUser

# Create your models here.


class Collections(models.Model):
    title = models.CharField(max_length=30, unique=True)

    class Meta:
        ordering = ('id', )

    def __str__(self):
        return self.title


class Products(models.Model):
    owner = models.ForeignKey(GiftUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name='Название', blank=False, null=False)
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    photo = models.ImageField(upload_to='gift_photos', verbose_name='Фото', blank=True)
    link = models.URLField(verbose_name='Ссылка', blank=True)
    price = models.FloatField(verbose_name='Цена', blank=True, null=True)
    collection = models.ForeignKey(Collections, on_delete=models.PROTECT, default=1)

    class Meta:
        ordering = ('id', )

    def __str__(self):
        return self.name
