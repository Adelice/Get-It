# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-30 11:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getapp', '0002_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_store',
            field=models.ManyToManyField(to='getapp.Store', verbose_name='availability(ies) in store(s)'),
        ),
    ]