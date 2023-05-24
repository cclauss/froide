# Generated by Django 3.2.8 on 2022-02-15 14:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0032_auto_20211203_1058"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="organization",
            new_name="organization_name",
        ),
        migrations.AlterField(
            model_name="user",
            name="language",
            field=models.CharField(
                choices=[("de", "German"), ("en", "English")],
                default="de",
                help_text="Determines the default language of communication with you.",
                max_length=10,
                verbose_name="Language",
            ),
        ),
    ]
