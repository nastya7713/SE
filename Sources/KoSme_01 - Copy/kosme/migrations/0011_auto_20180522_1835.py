# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-22 15:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kosme', '0010_auto_20180522_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
