# Generated by Django 2.1.7 on 2019-05-29 04:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='giftuser',
            name='active_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 16, 4, 2, 16, 66684, tzinfo=utc)),
        ),
    ]