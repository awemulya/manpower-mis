from django.contrib import admin

# Register your models here.
from .models import PassportInfo


class PassportInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'passport_no', 'reference', 'document', 'cost', 'entry_date', 'status')
    list_filter = ('name','status')


admin.site.register(PassportInfo, PassportInfoAdmin)
