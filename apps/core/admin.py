from django.contrib import admin
from apps.core.models import Address


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    model = Address
    list_display = ["street", "number", "neighborhood", "city", "state"]
    search_fields = ["street", "number", "neighborhood", "city", "state"]
