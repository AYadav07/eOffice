from os import supports_bytes_environ
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from accounts.models import Account,Department,Director,Creator



# Register your models here.

class AccountAdmin(UserAdmin):
    list_display =('email','username','first_name','last_name','department','date_joined','last_login','is_admin')
    search_fields = ('email','username','first_name','last_name')
    readonly_fields = ('date_joined','last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


'''class DepartmentAdmin(UserAdmin):
    list_display =('dept_name','dept_HOD')
    search_fields = ('dept_name','dept_HOD')
    readonly_fields = ('dept_HOD','dept_HOD')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()'''


class DirectorAdmin(admin.ModelAdmin):
    def has_add_permission(self,request):
        count=Director.objects.all().count()
        if count==0:
            return True
        return False


class DepartmentAdmin(admin.ModelAdmin):
    def get_form(self,request,obj=None,**kwargs):
        self.instance=obj
        return super(DepartmentAdmin,self).get_form(request,obj=obj,**kwargs)

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        if db_field.name=='dept_HOD' and self.instance:
            kwargs['queryset'] = Account.objects.filter(department__dept_id=self.instance.pk)
        return super(DepartmentAdmin,self).formfield_for_foreignkey(db_field, request=request, **kwargs)
    




admin.site.register(Account,AccountAdmin)

admin.site.register(Department,DepartmentAdmin)

admin.site.register(Director,DirectorAdmin)

admin.site.register(Creator)
