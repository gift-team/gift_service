# Generated by Django 2.1.7 on 2019-05-20 13:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('friendsapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friendshiprequest',
            name='to_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friendship_request_received', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='friendshiprequest',
            unique_together=set(),
        ),
    ]
