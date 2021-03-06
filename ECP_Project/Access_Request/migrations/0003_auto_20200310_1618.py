# -*- coding: utf-8 -*-
# Generated by Django 3.1.10.17 on 2020-03-10 13:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Access_Request', '0002_auto_20200310_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ep_keys',
            name='comment',
            field=models.TextField(blank=True, verbose_name='Комментарий'),
        ),
        migrations.AlterField(
            model_name='ep_keys',
            name='user_photo',
            field=models.FileField(blank=True, upload_to='', verbose_name='Фото пользователя'),
        ),
    ]
