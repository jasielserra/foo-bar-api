from django.contrib.admin import ModelAdmin, register
from zipbank.core.models import Item
# Register your models here.

@register(Item)
class ItemAdmin(ModelAdmin):
    list_display = ('product','value','qty')