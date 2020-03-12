# -*- coding: utf-8 -*-
# Generated by Django 3.1.10.17 on 2020-03-12 06:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Access_Request', '0006_auto_20200311_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ep_keys',
            name='license_csp',
            field=models.CharField(blank=True, max_length=120, verbose_name='Лицензия CSP'),
        ),
        migrations.AlterField(
            model_name='ep_keys',
            name='license_ocsp',
            field=models.CharField(blank=True, max_length=120, verbose_name='Лицензия OCSP'),
        ),
        migrations.AlterField(
            model_name='ep_keys',
            name='license_tsp',
            field=models.CharField(blank=True, max_length=120, verbose_name='Лицензия TSP'),
        ),
    ]
