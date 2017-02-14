# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-08 04:57
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopUp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('receipt', models.ImageField(upload_to='receipts/', verbose_name='Bukti Bayar')),
                ('status', models.CharField(choices=[('p', 'pending'), ('v', 'valid'), ('i', 'invalid')], max_length=1)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('validated_at', models.DateTimeField(auto_now=True)),
                ('checked_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='member',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Alamat'),
        ),
        migrations.AlterField(
            model_name='member',
            name='phone',
            field=models.CharField(max_length=20, verbose_name='Nomor Telepon'),
        ),
        migrations.AlterField(
            model_name='member',
            name='prof_pic',
            field=models.ImageField(blank=True, null=True, upload_to='prof_pics/', verbose_name='Foto Profil'),
        ),
        migrations.AddField(
            model_name='topup',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.Member'),
        ),
    ]
