# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-23 13:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('micro_admin', '0016_groupmemberloanaccount_account_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupmemberloanaccount',
            name='account_no',
            field=models.CharField(max_length=50),
        ),
    ]
