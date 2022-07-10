from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import credit, fast_tag


# Register your models here.

class credit_admin(admin.ModelAdmin):
    list_display = ['card_no', 'card_name', 'card_expiry']


class fast_tag_admin(admin.ModelAdmin):
    list_display = ['name', 'vehicle_no', 'registered_bank', 'address']


admin.site.register(credit,credit_admin)
admin.site.register(fast_tag,fast_tag_admin)