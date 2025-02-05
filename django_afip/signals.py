import datetime

from django.db.models.signals import post_save
from django.db.models.signals import pre_save
from django.dispatch import receiver

from django_afip import exceptions
from django_afip import models


@receiver(pre_save, sender=models.TaxPayer)
def update_certificate_expiration(sender, instance: models.TaxPayer, **kwargs):
    if instance.certificate:
        instance.certificate_expiration = instance.get_certificate_expiration()


@receiver(post_save, sender=models.ReceiptPDF)
def generate_receipt_pdf(sender, instance: models.ReceiptPDF, **kwargs):
    if not instance.pdf_file:
        if instance.receipt.ready_to_print:
            instance.save_pdf(save_model=True)


@receiver(pre_save, sender=models.Receipt)
def save_caea_data(sender, instance: models.TaxPayer, **kwargs):
    if "CAEA" not in instance.point_of_sales.issuance_type:
        return

    if instance.caea == "" or instance.caea == None:
        date = datetime.datetime.now()
        period = date.today().strftime("%Y%m")
        order = 1
        if date.day > 15:
            order = 2
        caea = models.Caea.objects.active().filter(
            taxpayer=instance.point_of_sales.owner,
            period=int(period),
            order=order,
        )
        if caea.count() != 1:
            raise exceptions.CaeaCountError
        else:
            if instance.caea == None or instance.caea == "":
                instance.caea = caea[0]

        if instance.receipt_number == None or instance.receipt_number == "":

            last_number = (
                models.Receipt.objects.filter(
                    point_of_sales=instance.point_of_sales,
                    receipt_type=instance.receipt_type,
                )
                .order_by("-receipt_number")
                .values_list("receipt_number", flat=True)
                .first()
            )

            if last_number == None:  # First record on the db
                last_number = 0

            correct_number = last_number + 1
            instance.receipt_number = correct_number
