# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-02 14:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('overview', '0002_auto_20171102_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='hyperlink',
            field=models.CharField(max_length=1024, null=True),
        ),
    ]
