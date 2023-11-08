from django.contrib import admin
from urls.models import UrlModel

# Register your models here.
@admin.register(UrlModel)
class UrlAdmin(admin.ModelAdmin):
    list_display = ('id', 'creation_date', 'url')
    list_filter = ('creation_date',)