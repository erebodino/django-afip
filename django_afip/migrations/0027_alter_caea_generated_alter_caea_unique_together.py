# Generated by Django 4.0.8 on 2022-10-15 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('afip', '0026_merge_20220922_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caea',
            name='generated',
            field=models.DateTimeField(help_text='When this CAEA was generated', verbose_name='generated'),
        ),
        migrations.AlterUniqueTogether(
            name='caea',
            unique_together={('order', 'period', 'taxpayer')},
        ),
    ]
