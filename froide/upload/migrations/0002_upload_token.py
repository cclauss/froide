# Generated by Django 2.2.4 on 2019-10-21 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload',
            name='token',
            field=models.UUIDField(blank=True, null=True),
        ),
    ]
