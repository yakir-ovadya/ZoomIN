# Generated by Django 3.1.3 on 2021-01-04 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0015_schedule_form'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='schedule_form',
            new_name='schedule',
        ),
    ]
