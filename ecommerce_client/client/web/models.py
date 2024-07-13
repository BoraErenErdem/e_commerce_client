from django.db import models
from socket import gethostname, gethostbyname


class Status(models.TextChoices):
    ACTIVE = 'Active', 'Active'
    MODIFIED = 'Modified', 'Modified'
    PASSIVE = 'Passive', 'Passive'


class Category(models.Model):
    class Meta:
        db_table = 'store_category'

    name = models.CharField(max_length=250, unique=True, db_index=True)
    slug = models.SlugField(max_length=250, unique=True)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.ACTIVE)
    ip_address = models.GenericIPAddressField(max_length=50, default=gethostbyname(gethostname()))
    machine_name = models.CharField(max_length=50, default=gethostname())
