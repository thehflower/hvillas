from django.contrib import admin

from villas.models import Villa,Resident
# Register your models here.


class ResidentInline(admin.StackedInline):
    model = Resident
class VillaAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
        (None,               {'fields': ['feet']}),
    ]
    inlines = [ResidentInline]



admin.site.register(Villa, VillaAdmin)
