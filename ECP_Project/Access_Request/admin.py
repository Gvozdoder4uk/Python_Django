from django.contrib import admin
from .models import EP_Keys, Services
from django.conf.locale.es import formats as es_formats

es_formats.DATETIME_FORMAT = "d M Y H:i:s"
# Register your models here.


# admin.site.register(EP_Keys)
admin.site.register(Services)


class EP_Keys_Admin(admin.ModelAdmin):
    list_display = ('owner', 'id_key')


admin.site.register(EP_Keys, EP_Keys_Admin)
