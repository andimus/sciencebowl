# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-12-09 04:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0005_auto_20161207_1026'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='tossup_or_bonus',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='comp',
            field=models.CharField(blank=True, default=None, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='subject',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='subtopic',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
    ]
