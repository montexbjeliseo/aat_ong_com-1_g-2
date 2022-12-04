# Generated by Django 3.2 on 2022-12-04 00:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('body', models.TextField()),
                ('author', models.CharField(blank=True, max_length=50, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='noticias')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='noticias.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('noticias', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='noticias.noticia')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuarios_comentarios', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
