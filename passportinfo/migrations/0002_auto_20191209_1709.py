# Generated by Django 3.0 on 2019-12-09 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('passportinfo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='passportinfo',
            old_name='referene',
            new_name='reference',
        ),
    ]