# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-09 16:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adopcion', '0003_auto_20180307_2340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
