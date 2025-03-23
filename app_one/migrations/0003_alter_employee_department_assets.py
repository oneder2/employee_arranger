# Generated by Django 4.1 on 2025-01-26 21:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app_one", "0002_remove_employee_departure_employee_department"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employee",
            name="department",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="app_one.department",
                verbose_name="department",
            ),
        ),
        migrations.CreateModel(
            name="Assets",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "phone_num",
                    models.CharField(max_length=11, verbose_name="Phont_num"),
                ),
                (
                    "status",
                    models.IntegerField(
                        choices=[(1, "has_been_occupied"), (2, "not_been_occupied")],
                        verbose_name="Usage_condition",
                    ),
                ),
                ("times", models.DateField(verbose_name="Created_time")),
                ("price", models.CharField(max_length=64, verbose_name="Price")),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="app_one.employee",
                    ),
                ),
            ],
        ),
    ]
