# Generated by Django 3.2 on 2022-12-12 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='usuarios'),
        ),
    ]
