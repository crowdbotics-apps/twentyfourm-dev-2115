# Generated by Django 2.2.11 on 2020-03-24 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_load_initial_data"),
    ]

    operations = [
        migrations.CreateModel(
            name="TThgh",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("hghg", models.BigIntegerField()),
            ],
        ),
    ]
