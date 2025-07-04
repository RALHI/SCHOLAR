# Generated by Django 5.2.3 on 2025-07-05 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("indexapp", "0002_team"),
    ]

    operations = [
        migrations.CreateModel(
            name="UpcomingEvents",
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
                ("cateory", models.CharField(max_length=100)),
                ("title", models.CharField(max_length=100)),
                ("date", models.DateField()),
                ("time", models.TimeField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                "verbose_name_plural": "Upcoming Events",
            },
        ),
    ]
