# Generated by Django 4.1.1 on 2022-09-07 13:01

import django.utils.timezone
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("afip", "0015_alter_caea_expires_alter_caea_final_date_inform_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="receipt",
            name="generated",
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now,
                verbose_name="Time when the receipt was created",
            ),
            preserve_default=False,
        ),
    ]
