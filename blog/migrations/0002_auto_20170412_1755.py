# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-12 12:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reminder',
            name='createdTime',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 12, 12, 25, 23, 670673, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='reminder',
            name='modifiedTime',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 12, 12, 25, 23, 670673, tzinfo=utc)),
        ),
    ]