# Generated by Django 4.1 on 2022-08-17 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='address',
        ),
    ]