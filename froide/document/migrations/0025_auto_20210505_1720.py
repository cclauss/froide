# Generated by Django 3.1.8 on 2021-05-05 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0024_auto_20210323_1404'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='data',
            field=models.JSONField(blank=True, default=dict),
        ),
        migrations.AddField(
            model_name='documentcollection',
            name='settings',
            field=models.JSONField(blank=True, default=dict),
        ),
    ]
