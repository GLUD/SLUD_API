# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-01 22:22
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('slud', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='charla',
            name='timefecha',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 1, 22, 22, 30, 264207, tzinfo=utc)),
            preserve_default=False,
        ),
    ]