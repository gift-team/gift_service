# Generated by Django 2.1.7 on 2019-05-24 07:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0012_auto_20190522_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='giftuser',
            name='active_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 11, 7, 16, 1, 334849, tzinfo=utc)),
        ),
    ]
