# Generated by Django 4.1.1 on 2022-09-13 19:54

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("afip", "0020_alter_receipt_caea"),
    ]

    operations = [
        migrations.AlterField(
            model_name="receiptvalidation",
            name="cae_expiration",
            field=models.DateField(
                blank=True,
                help_text="The CAE expiration as returned by the AFIP.",
                null=True,
                verbose_name="cae expiration",
            ),
        ),
    ]