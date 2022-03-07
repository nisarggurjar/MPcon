from django.contrib import admin
from .models import Address, UserInfo, Warehouses

admin.site.register(UserInfo)
admin.site.register(Address)
admin.site.register(Warehouses)