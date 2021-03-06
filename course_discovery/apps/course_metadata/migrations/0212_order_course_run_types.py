# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-11-06 20:36
from __future__ import unicode_literals

from django.db import migrations
import sortedm2m.fields
from sortedm2m.operations import AlterSortedManyToManyField


class Migration(migrations.Migration):

    dependencies = [
        ('course_metadata', '0211_remove_course_has_ofac_restrictions'),
    ]

    operations = [
        AlterSortedManyToManyField(
            model_name='coursetype',
            name='course_run_types',
            field=sortedm2m.fields.SortedManyToManyField(help_text='Sets the order for displaying Course Run Types.', to='course_metadata.CourseRunType'),
        ),
    ]
