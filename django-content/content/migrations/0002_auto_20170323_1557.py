# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-23 15:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='source',
            name='title',
            field=models.CharField(db_index=True, max_length=200),
        ),
    ]
