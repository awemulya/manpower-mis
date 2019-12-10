from django.contrib import admin
from datetime import date 

# Register your models here.
from .models import PassportInfo, CountryCategory, Country


class PassportInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'passport_no', 'reference', 'country', 'pp_photo', 'passport', 'cost', 'entry_date', 'status')
    list_filter = ('name','status')


admin.site.register(PassportInfo, PassportInfoAdmin)
admin.site.register(CountryCategory)
admin.site.register(Country)
