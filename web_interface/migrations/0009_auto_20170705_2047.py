# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-05 20:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_interface', '0008_auto_20170705_1945'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='blance',
            new_name='balance',
        ),
    ]
