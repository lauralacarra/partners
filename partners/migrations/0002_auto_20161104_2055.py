# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-04 19:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='partner',
            old_name='last_name',
            new_name='lastname',
        ),
        migrations.AddField(
            model_name='partner',
            name='partner_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
