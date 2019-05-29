from django.db import models
from authapp.models import GiftUser
from django.conf import settings

# Create your models here.


class Collections(models.Model):
    title = models.CharField(max_length=30, unique=True)

# TODO На подумать - как правильно делать сортировку
    class Meta:
        ordering = ('title', )

    def __str__(self):
        return self.title


class Gift(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name='Название', blank=False, null=False)
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    photo = models.ImageField(upload_to='gift_photos', verbose_name='Фото', blank=True, null=True)
    link = models.URLField(verbose_name='Ссылка', blank=True, null=True)
    price = models.FloatField(verbose_name='Цена', blank=True, null=True)

# TODO На подумать - как правильно делать сортировку
    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.name
