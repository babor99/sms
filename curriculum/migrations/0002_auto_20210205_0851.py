# Generated by Django 3.1 on 2021-02-05 02:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lesson',
            old_name='subjec',
            new_name='subject',
        ),
    ]
