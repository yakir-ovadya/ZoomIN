# Generated by Django 3.1.3 on 2020-12-31 13:02

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0005_auto_20201231_1456'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Userprofile',
            new_name='Usersprofile',
        ),
    ]