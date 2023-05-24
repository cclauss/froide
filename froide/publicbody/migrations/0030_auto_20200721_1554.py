# Generated by Django 3.0.8 on 2020-07-21 13:54

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("publicbody", "0029_auto_20200703_2032"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="publicbody",
            options={
                "ordering": ("name",),
                "permissions": (("moderate", "Can moderate public bodies"),),
                "verbose_name": "Public Body",
                "verbose_name_plural": "Public Bodies",
            },
        ),
    ]
