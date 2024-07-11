# Generated by Django 5.0.7 on 2024-07-11 15:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RegisteredUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('peran', models.CharField()),
                ('nama', models.CharField()),
                ('umur', models.IntegerField()),
                ('domisili', models.CharField()),
                ('golongan_darah', models.CharField()),
                ('status_ibu', models.CharField(blank=True, default=None, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Bayi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('umur', models.IntegerField()),
                ('jenis_kelamin', models.CharField()),
                ('orang_tua', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='authentication.registereduser')),
            ],
        ),
    ]