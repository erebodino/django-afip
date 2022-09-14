# Generated by Django 4.1.1 on 2022-09-08 19:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("afip", "0016_receipt_generated"),
    ]

    operations = [
        migrations.AddField(
            model_name="receipt",
            name="caea",
            field=models.ForeignKey(
                blank=True,
                help_text="CAEA in case that the receipt must contain it",
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="afip.caea",
            ),
        ),
        migrations.AddField(
            model_name="receiptvalidation",
            name="caea",
            field=models.BooleanField(
                default=False,
                help_text="Indicate if the validation was from a CAEA receipt, in that case the field cae contains the CAEA number",
                verbose_name="is_caea",
            ),
        ),
    ]
