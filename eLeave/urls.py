from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('',views.eleave_home,name='eleave_home'),
    path('leaveapplication',views.leave_app,name='leaveApplication'),
    path('hod_forward/<int:id>',views.hod_forward,name='hod_forward'),
    path('hod_decline/<int:id>',views.hod_decline,name='hod_decline'),
    path('director_approve/<int:id>',views.director_approve,name='director_approve'),
    path('director_reject/<int:id>',views.director_reject,name='director_reject'),
]