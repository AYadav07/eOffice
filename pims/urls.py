from django.urls import path
from django.urls.conf import include
from . import views
#from .views import PimsView,PimsThankYouView

urlpatterns = [
    path('',views.pims_home,name='pims_home'),
    path('pims_details/<int:id>',views.pims_details,name='pims_details'),
    #path('creator_add',PimsView.as_view(),name='creator_add'),
    #path('thank-you/', PimsThankYouView.as_view(), name="thank_you"),
    path('add_details/<int:id>',views.add_details,name='add_details'),
    path('add_details2/<int:id>',views.add_details2,name='add_details2'),
    path('add_details3/<int:id>',views.add_details3,name='add_details3'),
    path('view_1/<int:id>',views.view_1,name='view_1'),
    path('view_2/<int:id>',views.view_2,name='view_2'),
    path('view_3/<int:id>',views.view_3,name='view_3'),
    path('edit_1/<int:id>',views.edit_1,name='edit_1'),
    path('edit_2/<int:id>',views.edit_2,name='edit_2'),
    path('edit_3/<int:id>',views.edit_3,name='edit_3'),
    path('director_verify/<int:id>',views.director_verify,name='director_verify'),


    ]