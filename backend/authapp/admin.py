from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import ugettext_lazy as _

from .models import GiftUser, Address, AddressName, Country, Region, City, Street, Building, Flat, AddressList


@admin.register(GiftUser)
class UserAdmin(DjangoUserAdmin):
    """Define admin model for custom User model with no email field."""

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'middle_name', 'last_name', 'address_list',
                                         'login', 'birthdate', 'phone', 'gender', 'avatar')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)


admin.site.register(Address)
admin.site.register(AddressList)
admin.site.register(AddressName)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Region)
admin.site.register(Street)
admin.site.register(Building)
admin.site.register(Flat)
