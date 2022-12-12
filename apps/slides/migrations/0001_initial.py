# Generated by Django 3.2 on 2022-12-12 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(blank=True, max_length=250, null=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='slides')),
                ('creado', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
