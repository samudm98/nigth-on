from django.db import models


class Pub(models.Model):
    name = models.CharField(max_length=50, blank=False)
    address = models.CharField(max_length=255, blank=True)
    latitude = models.FloatField(blank=False, null=False)
    longitude = models.FloatField(blank=False, null=False)
    open = models.TimeField(blank=True)
    close = models.TimeField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    cheap = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return self.name


class ImageModel(models.Model):
    image = models.ImageField(upload_to='img', null=False)
    pub = models.ForeignKey(Pub, null=False, on_delete=models.CASCADE)
