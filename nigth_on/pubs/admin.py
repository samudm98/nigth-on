from nigth_on.pubs.models import Pub
from django.contrib import admin


@admin.register(Pub)
class PubAdmin(admin.ModelAdmin):
    pass
