# Generated by Django 4.0.4 on 2022-05-23 02:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comensales',
            name='Contrasena',
        ),
        migrations.RemoveField(
            model_name='comensales',
            name='Email',
        ),
    ]
