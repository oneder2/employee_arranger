# Generated by Django 4.1 on 2025-01-27 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_one", "0005_rename_times_assets_create_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="assets",
            name="phone_num",
            field=models.CharField(max_length=11, verbose_name="Phone_num"),
        ),
    ]
