# Generated by Django 2.1.7 on 2019-05-24 08:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0007_auto_20190514_1228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='giftuser',
            name='active_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 11, 8, 52, 21, 323403, tzinfo=utc)),
        ),
    ]
