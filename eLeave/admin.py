from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from eLeave.models import Leave
'''from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from accounts.models import Account


# Register your models here.

class EleaveAdmin(UserAdmin):
    list_display =('email','username','first_name','last_name','department','por','date_joined','last_login','is_admin')
    search_fields = ('email','username','first_name','last_name')
    readonly_fields = ('date_joined','last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(,AccountAdmin)

class LeaveAdmin(UserAdmin):
    list_display =('start_date','end_date','reason','applied_date')
    search_fields = ('start_date')
    readonly_fields = ('applied_date')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()'''


admin.site.register(Leave)