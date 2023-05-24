# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-30 00:28
from __future__ import unicode_literals

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("publicbody", "0003_auto_20160123_1336"),
    ]

    operations = [
        migrations.AlterField(
            model_name="publicbody",
            name="_created_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="public_body_creators",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Created by",
            ),
        ),
        migrations.AlterField(
            model_name="publicbody",
            name="_updated_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="public_body_updaters",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Updated by",
            ),
        ),
    ]
