# Generated by Django 5.2.1 on 2025-05-11 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_alter_usuario_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='correo_verificado',
        ),
    ]
