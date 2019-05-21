# Generated by Django 2.1.7 on 2019-05-11 16:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_auto_20190510_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='giftuser',
            name='active_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 28, 16, 3, 28, 143611, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='giftuser',
            name='age',
            field=models.DateField(blank=True, null=True, verbose_name='возраст'),
        ),
    ]