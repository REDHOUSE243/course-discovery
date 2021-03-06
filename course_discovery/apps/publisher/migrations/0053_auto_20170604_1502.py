# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-04 15:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publisher', '0052_auto_20170529_1002'),
    ]

    operations = [
        migrations.AddField(
            model_name='courserun',
            name='is_professional_certificate',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='courserun',
            name='professional_certificate_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='historicalcourserun',
            name='is_professional_certificate',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='historicalcourserun',
            name='professional_certificate_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
