# -*- coding: utf-8 -*-
# Generated by Django 3.1.10.17 on 2020-03-10 13:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Access_Request', '0003_auto_20200310_1618'),
    ]

    operations = [
        migrations.AddField(
            model_name='ep_keys',
            name='license_csp',
            field=models.CharField(default=0, max_length=120, verbose_name='Лицензия CSP'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ep_keys',
            name='license_ocsp',
            field=models.CharField(default=0, max_length=120, verbose_name='Лицензия OCSP'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ep_keys',
            name='license_tsp',
            field=models.CharField(default=0, max_length=120, verbose_name='Лицензия TSP'),
            preserve_default=False,
        ),
    ]
