from django.db import models

from nigth_on.pubs.models import Pub


class Product(models.Model):
    name = models.CharField(max_length=50, blank=False)
    price = models.FloatField(null=False, blank=False)
    description = models.CharField(max_length=50, blank=False)
    image = models.ImageField(upload_to='img', null=False)
    is_service = models.BooleanField(default=False, null=False)
    pub = models.ForeignKey(Pub, null=False, on_delete=models.CASCADE, related_name="products")
