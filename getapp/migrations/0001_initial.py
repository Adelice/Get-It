# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-25 15:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=30)),
                ('product_image', models.ImageField(upload_to='images/')),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SuperMarket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('market_name', models.CharField(max_length=30)),
                ('market_image', models.ImageField(upload_to='images/')),
                ('market_location', models.CharField(max_length=50)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='getapp.Product')),
            ],
        ),
        migrations.AddField(
            model_name='location',
            name='supermarkerk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='getapp.SuperMarket'),
        ),
    ]