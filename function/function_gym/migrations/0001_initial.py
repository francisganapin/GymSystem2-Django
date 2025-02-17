# Generated by Django 4.2 on 2025-02-17 03:56

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="GymEquipment",
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
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("stock", models.IntegerField()),
                (
                    "picture",
                    models.ImageField(
                        blank=True, null=True, upload_to="equipment-picture/"
                    ),
                ),
            ],
            options={
                "db_table": "gym_equipment_record",
            },
        ),
    ]
