from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from contacts.utils import STATE_CHOICES, slug_gen
from autoslug import AutoSlugField


class Contact(models.Model):
    """
     Contact Model includes:
     First name
     Last name
     Phone #
     Phone type i.e. cell, home, etc.
     Address Information
    """
    PHONE_CHOICES = [
        ("MOBILE", "Mobile"),
        ("WORK", "Work"),
        ("HOME", "Home")
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = PhoneNumberField()
    phone_type = models.CharField(max_length=35, choices=PHONE_CHOICES)
    street_address1 = models.CharField(max_length=100)
    street_address2 = models.CharField(max_length=100, blank=True, default="")
    city = models.CharField(max_length=100, default="")
    state = models.CharField(max_length=50, choices=STATE_CHOICES)
    zip_code = models.CharField(max_length=10)
    slug = AutoSlugField(populate_from=slug_gen, unique=True)
