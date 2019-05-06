from django.contrib import admin

from addressapp.models import Address, AddressName, Country, Region, City, Street, Building

# Register your models here.

admin.site.register(Address)
admin.site.register(AddressName)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Region)
admin.site.register(Street)
admin.site.register(Building)


