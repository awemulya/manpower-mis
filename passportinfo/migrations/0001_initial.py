# Generated by Django 3.0 on 2019-12-10 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='CountryCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PassportInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('passport_no', models.IntegerField()),
                ('reference', models.CharField(max_length=255)),
                ('pp_photo', models.FileField(upload_to='photos')),
                ('qualification_certificate', models.FileField(upload_to='qualification_certificate')),
                ('working_certificate', models.FileField(upload_to='working_certificate')),
                ('passport', models.FileField(upload_to='passport')),
                ('cost', models.IntegerField()),
                ('entry_date', models.DateField()),
                ('status', models.CharField(choices=[('On Hold', 'On Hold'), ('Completed', 'Completed')], max_length=255)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='passportinfo', to='passportinfo.Country')),
            ],
            options={
                'ordering': ['-entry_date'],
            },
        ),
        migrations.AddField(
            model_name='country',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='country', to='passportinfo.CountryCategory'),
        ),
    ]
