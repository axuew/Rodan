# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-29 13:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rodan', '0020_auto_20200420_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resourcelabel',
            name='name',
            field=models.CharField(max_length=36, unique=True),
        ),
    ]