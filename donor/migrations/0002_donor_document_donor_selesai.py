# Generated by Django 5.0.7 on 2024-07-12 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='donor',
            name='document',
            field=models.FileField(blank=True, default=None, null=True, upload_to='donor_documents/'),
        ),
        migrations.AddField(
            model_name='donor',
            name='selesai',
            field=models.BooleanField(blank=True, default=0, null=True),
        ),
    ]
