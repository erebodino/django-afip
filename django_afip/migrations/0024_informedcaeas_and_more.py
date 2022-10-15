# Generated by Django 4.1.1 on 2022-09-21 20:45

import django.db.models.deletion
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("afip", "0023_alter_receipt_caea"),
    ]

    operations = [
        migrations.CreateModel(
            name="InformedCaeas",
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
                ("processed_date", models.DateTimeField(verbose_name="processed date")),
                (
                    "caea",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="informed",
                        to="afip.caea",
                    ),
                ),
                (
                    "pos",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="informed",
                        to="afip.pointofsales",
                    ),
                ),
            ],
        ),
        migrations.AddConstraint(
            model_name="informedcaeas",
            constraint=models.UniqueConstraint(
                fields=("pos", "caea"), name="unique_migration_pos_caea_combination"
            ),
        ),
    ]