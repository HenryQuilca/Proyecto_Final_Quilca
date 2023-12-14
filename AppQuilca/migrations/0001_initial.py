# Generated by Django 4.2.7 on 2023-12-14 18:23

import datetime
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
            name='Racquet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raqueta', models.CharField(max_length=50)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=5)),
                ('estado', models.CharField(choices=[('Used', 'Usado'), ('New', 'Nuevo')], max_length=10, null=True)),
                ('fecha_creacion', models.DateTimeField(blank=True, default=datetime.datetime(2023, 12, 14, 18, 23, 15, 187054, tzinfo=datetime.timezone.utc))),
                ('stock', models.IntegerField()),
                ('descripcion', models.CharField(max_length=255)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='raquetas')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.CharField(max_length=255)),
                ('fecha_creacion', models.DateTimeField(blank=True, default=datetime.datetime(2023, 12, 14, 18, 23, 15, 188058, tzinfo=datetime.timezone.utc))),
                ('raqueta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='AppQuilca.racquet')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Avatar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='avatares')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
