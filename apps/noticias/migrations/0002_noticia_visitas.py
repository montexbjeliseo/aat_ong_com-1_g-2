# Generated by Django 3.2 on 2022-12-06 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='visitas',
            field=models.IntegerField(default=0),
        ),
    ]