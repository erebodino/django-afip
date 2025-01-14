# Generated by Django 4.1.1 on 2022-10-17 15:40

import datetime

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("afip", "0029_alter_receipt_generated"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="caea",
            name="final_date_inform",
        ),
        migrations.AddField(
            model_name="caea",
            name="report_deadline",
            field=models.DateField(
                default=datetime.datetime(2022, 10, 17, 15, 40, 36, 849667),
                help_text="Activities for this CAEA must be informed before this date",
                verbose_name="report deadline",
            ),
            preserve_default=False,
        ),
    ]
