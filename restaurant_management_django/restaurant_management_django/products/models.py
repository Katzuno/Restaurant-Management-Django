from django.contrib.postgres.fields import HStoreField
from django.db import models
from django.db.models import CharField
from django.utils.translation import gettext_lazy as _


class NutritionalInformation(models.Model):
    class Status(models.TextChoices):
        INACTIVE = _('INACTIVE')
        ACTIVE = _('ACTIVE')

    name = CharField(_("Name of the product"), blank=False, max_length=255)
    description = CharField(_("Description of the product"), blank=True, max_length=1024)
    # Find a better solution
    #nutritional_values = CharField(_("Nutritional values of the product"), blank=True, max_length=1024)
    nutritional_values = HStoreField()
    status = models.CharField(
        max_length=8,
        choices=Status.choices,
        default=Status.ACTIVE,
    )
