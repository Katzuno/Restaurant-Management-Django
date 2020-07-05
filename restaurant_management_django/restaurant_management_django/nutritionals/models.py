from django.db import models
from django.db.models import CharField
from django.utils.translation import gettext_lazy as _


class NutritionalInformation(models.Model):
    name = CharField(_("Name of nutritional information"), blank=False, max_length=128)
    unit = CharField(_("Unit"), blank=False, max_length=16)
