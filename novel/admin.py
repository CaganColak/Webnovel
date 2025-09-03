from django.contrib import admin
from .models import Chapter,Novel,SiteSetting
# Register your models here.
admin.site.register(Chapter)
admin.site.register(Novel)

@admin.register(SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
    list_display = ("site_name",)