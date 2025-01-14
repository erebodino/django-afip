# Generated by Django 4.1.1 on 2022-09-06 15:24

import django.core.validators
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("afip", "0012_alter_caea_caea_code"),
    ]

    operations = [
        migrations.AlterField(
            model_name="caea",
            name="caea_code",
            field=models.PositiveBigIntegerField(
                help_text="CAEA code to operate offline AFIP",
                unique=True,
                validators=[
                    django.core.validators.RegexValidator(regex="[0-9]{14}"),
                    django.core.validators.MaxValueValidator(99999999999999),
                ],
            ),
        ),
    ]
