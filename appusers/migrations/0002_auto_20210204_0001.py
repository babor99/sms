# Generated by Django 3.1 on 2021-02-03 18:01

import appusers.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appusers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to=appusers.models.path_and_rename),
        ),
    ]
