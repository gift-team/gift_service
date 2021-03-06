# Generated by Django 2.1.7 on 2019-05-29 04:02

import authapp.models
import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='GiftUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('middle_name', models.CharField(blank=True, max_length=150, verbose_name='отчество')),
                ('country', models.CharField(blank=True, max_length=30, null=True, verbose_name='название страны')),
                ('region', models.CharField(blank=True, max_length=30, null=True, verbose_name='область')),
                ('city', models.CharField(blank=True, max_length=30, null=True, verbose_name='населенный пункт')),
                ('street', models.CharField(blank=True, max_length=30, null=True, verbose_name='улица')),
                ('building', models.CharField(blank=True, max_length=7, null=True, verbose_name='дом')),
                ('flat', models.IntegerField(blank=True, null=True, verbose_name='квартира')),
                ('login', models.CharField(blank=True, max_length=20, null=True, verbose_name='логин')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='client_avatars')),
                ('birthdate', models.DateField(blank=True, null=True, verbose_name='дата рождения')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='почта')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, verbose_name='телефон')),
                ('gender', models.CharField(blank=True, choices=[('M', 'Мужчина'), ('W', 'Женщина')], max_length=1, verbose_name='пол')),
                ('active_key', models.CharField(blank=True, max_length=128, verbose_name='код подтверждения')),
                ('active_key_expires', models.DateTimeField(default=datetime.datetime(2019, 7, 16, 4, 2, 1, 670858, tzinfo=utc))),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', authapp.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='AddressList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='название адреса')),
                ('country', models.CharField(max_length=30, verbose_name='название страны')),
                ('region', models.CharField(max_length=30, verbose_name='область')),
                ('city', models.CharField(max_length=30, verbose_name='населенный пункт')),
                ('street', models.CharField(max_length=30, verbose_name='улица')),
                ('building', models.CharField(max_length=7, verbose_name='дом')),
                ('flat', models.IntegerField(verbose_name='квартира')),
            ],
        ),
    ]
