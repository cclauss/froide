# Generated by Django 3.0.8 on 2020-08-23 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foirequest', '0046_foievent_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foirequest',
            name='visibility',
            field=models.SmallIntegerField(choices=[(0, 'Invisible'), (1, 'Visible to requester'), (2, 'Visible to public')], default=0, verbose_name='Visibility'),
        ),
    ]