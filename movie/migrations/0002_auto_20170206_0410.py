# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-06 04:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='cover',
            field=models.ImageField(blank=True, default='no-image.png', upload_to='movie_covers/'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='deskripsi'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='yang posting'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='show_from',
            field=models.DateField(verbose_name='tayang dari'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='show_until',
            field=models.DateField(verbose_name='tayang hingga'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(max_length=200, verbose_name='judul'),
        ),
    ]