from django.contrib import admin
from .models import File,Docs,DocAction,FileAction
# Register your models here.
admin.site.register(File)
admin.site.register(Docs)
admin.site.register(FileAction)
admin.site.register(DocAction)