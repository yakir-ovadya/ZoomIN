# Generated by Django 3.1.2 on 2020-12-14 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administrator',
            name='code_admin',
            field=models.CharField(max_length=20),
        ),
    ]
