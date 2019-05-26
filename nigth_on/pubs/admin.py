from nigth_on.pubs.models import Pub, ImageModel
from django.contrib import admin


@admin.register(Pub)
class PubAdmin(admin.ModelAdmin):
    pass


@admin.register(ImageModel)
class ImageAdmin(admin.ModelAdmin):
    pass
