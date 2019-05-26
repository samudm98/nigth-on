from django.db import models
from rest_framework.compat import MinValueValidator, MaxValueValidator


class Pub(models.Model):
    name = models.CharField(max_length=50, blank=False)
    address = models.CharField(max_length=255, blank=True)
    latitude = models.FloatField(blank=False, null=False)
    longitude = models.FloatField(blank=False, null=False)
    open = models.TimeField(blank=True)
    close = models.TimeField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    cheap = models.IntegerField(blank=False, null=False, validators=[MinValueValidator(1), MaxValueValidator(3)])

    def __str__(self):
        return self.name + ' - ' + self.address


class ImageModel(models.Model):
    image = models.ImageField(upload_to='img', null=False)
    pub = models.ForeignKey(Pub, null=False, on_delete=models.CASCADE, related_name="images")

    def __str__(self):
        return self.image.name + ' -- ' + self.pub.name


class Comment(models.Model):
    name = models.CharField(max_length=128, blank=False)
    description = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='img', null=False)
    stars = models.IntegerField(blank=False, null=False, validators=[MinValueValidator(1), MaxValueValidator(5)])
    pub = models.ForeignKey(Pub, null=False, on_delete=models.CASCADE, related_name="comments")

