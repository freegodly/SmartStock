# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-30 01:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StockBasics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('industry', models.CharField(max_length=30)),
                ('area', models.CharField(max_length=30)),
                ('pe', models.FloatField()),
                ('outstanding', models.FloatField()),
                ('totals', models.FloatField()),
                ('totalAssets', models.FloatField()),
                ('liquidAssets', models.FloatField()),
                ('fixedAssets', models.FloatField()),
                ('reserved', models.FloatField()),
                ('reservedPerShare', models.FloatField()),
                ('eps', models.FloatField()),
                ('bvps', models.FloatField()),
                ('pb', models.FloatField()),
                ('timeToMarket', models.DateField()),
            ],
        ),
    ]