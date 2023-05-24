# Generated by Django 3.0.8 on 2020-07-10 15:49

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("foirequest", "0041_auto_20191024_2025"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="foirequest",
            options={
                "get_latest_by": "last_message",
                "ordering": ("-last_message",),
                "permissions": (
                    ("see_private", "Can see private requests"),
                    ("create_batch", "Create batch requests"),
                    ("moderate", "Can moderate requests"),
                ),
                "verbose_name": "Freedom of Information Request",
                "verbose_name_plural": "Freedom of Information Requests",
            },
        ),
    ]
