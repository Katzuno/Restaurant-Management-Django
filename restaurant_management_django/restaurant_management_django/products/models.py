import re

from django.contrib.postgres.fields import HStoreField
from django.db import models
from django.db.models import CharField
from django.utils.translation import gettext_lazy as _

from restaurant_management_django.nutritionals.models import NutritionalInformation


def validate_format(nutritional_values):
    for key in nutritional_values.keys():
        if not re.match(r"^[a-zA-Z\s\d]+\([a-zA-Z]+\)$", key):
            raise ValueError(_('Key \'' + key + '\' does not respect the format {String (unit)}'))


def validate_value_exists(new_nutritional_values):
    """
    @TODO: This function should be deleted if this will be used without Nutritional Values model
    :param new_nutritional_values:
    :return:
    """
    existing_nutritional_values = NutritionalInformation.objects.all().values_list('name', 'unit')
    start_char = '('
    end_char = ')'
    for nutritional_value in new_nutritional_values:
        start_char_position = nutritional_value.find(start_char)
        end_char_position = nutritional_value.rfind(end_char)
        unit = nutritional_value[start_char_position + len(start_char):end_char_position]
        nutritional_info_type = nutritional_value[:start_char_position].rstrip()

        if (nutritional_info_type, unit) not in existing_nutritional_values:
            raise ValueError(_("Nutritional value \'" + nutritional_info_type + "\' does not exists or it has "
                                                                              "a different unit. Please create it!"))


class Product(models.Model):
    class Status(models.TextChoices):
        INACTIVE = _('INACTIVE')
        ACTIVE = _('ACTIVE')

    name = CharField(_("Name of the product"), blank=False, max_length=255)
    description = CharField(_("Description of the product"), blank=True, max_length=1024)
    # Add constraints
    nutritional_values = HStoreField(_("Nutritional values of the product"), blank=True,
                                     validators=[validate_format, validate_value_exists])
    status = models.CharField(
        max_length=8,
        choices=Status.choices,
        default=Status.ACTIVE,
    )
