# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-29 16:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_pic', models.ImageField(blank=True, upload_to='stores/', verbose_name='logo/picture')),
                ('store_name', models.CharField(max_length=30, verbose_name='store')),
                ('store_location', models.CharField(max_length=30, verbose_name='location name')),
                ('store_address', models.CharField(max_length=200, verbose_name='Address')),
                ('store_city', models.CharField(max_length=30, verbose_name='city')),
            ],
            options={
                'ordering': ['store_name', 'store_city', 'store_location'],
            },
        ),
    ]
