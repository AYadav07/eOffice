from django.urls import path
from django.urls.conf import include
from . import views
from eOffice import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.efile_home,name='efile_home'),
    path('createfile',views.createfile,name='createfile'),
    path('open_file/<int:id>',views.open_file,name='open_file'),
    path('uploadfile/<int:id>',views.uploadfile,name='uploadfile'),
    path('sendfile/<int:id>',views.sendfile,name='sendfile'),
    path('opendoc/<int:id>',views.opendoc,name='opendoc'),
]

if settings.DEBUG :
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)