from django.contrib import admin

from prison.models import Warden, Armoury

# Register your models here.
admin.site.site_header = 'Prison Administration'
admin.site.site_title = 'Prison Administration'

class WardenAdmin(admin.ModelAdmin):
    list_display = ['FirstName','LastName']
    search_fields = ['FirstName','LastName']
    list_filter = ['Gender']
    list_per_page = 25

class ArmouryAdmin(admin.ModelAdmin):
    list_display = ['GunModel','created_at','status','updated_at']
    search_fields = ['GunModel']
    list_filter = ['status']
    list_per_page = 25
admin.site.register(Warden,WardenAdmin)
admin.site.register(Armoury,ArmouryAdmin)