from django.shortcuts import render,redirect
import datetime
from django.db.models import Q
from accounts.models import Department, Director
from eLeave.models import Leave

# Create your views here.

def eleave_home(request):
    curr_date=datetime.datetime.now().date()
    if Director.objects.filter(director__user_id=request.user.user_id).exists():
        leave_application_curr=Leave.objects.filter(start_date__gte=curr_date,is_forwarded=True,is_approved__isnull=True)
        leave_application=Leave.objects.filter(is_forwarded=True) & Leave.objects.filter(Q(start_date__lte=curr_date) | Q(is_approved__isnull=False))
        return render(request,'eleave/director_home.html',{'leave_application':leave_application,'leave_appication_curr':leave_application_curr})
    elif Department.objects.filter(dept_HOD__user_id=request.user.user_id).exists():
        leave_application_curr=Leave.objects.filter(user_id__department__dept_id=request.user.department.dept_id,start_date__gte=curr_date,is_forwarded__isnull=True)
        leave_application=Leave.objects.filter(user_id__department__dept_id=request.user.department.dept_id) & Leave.objects.filter(Q(start_date__lte=curr_date) | Q(is_forwarded__isnull=False))
        return render(request,'eleave/hod_home.html',{'leave_application':leave_application,'leave_appication_curr':leave_application_curr})
    else:
        leave_application_curr=Leave.objects.filter(user_id__user_id=request.user.user_id, start_date__gte=curr_date)
        leave_application=Leave.objects.filter(user_id__user_id=request.user.user_id,start_date__lte=curr_date)
        return render(request,'eleave/user_home.html',{'leave_application':leave_application,'leave_appication_curr':leave_application_curr})


def leave_app(request):
    n=""
    if request.method =='POST':
        user_id=request.user
        start_date=request.POST['start_date']
        end_date=request.POST['end_date']
        reason=request.POST['reason']


        new_leave= Leave(user_id=user_id,start_date=start_date,end_date=end_date,reason=reason)
        new_leave.save()
        n="Applied"
        return redirect("eleave_home")

    return render(request,'eleave/leaveapplication.html')

def hod_forward(request,id):
    leave=Leave.objects.get(leave_id=id)
    leave.is_forwarded=True
    leave.forwarded_date=datetime.datetime.now()
    leave.save()
    return redirect("eleave_home")


def hod_decline(request,id):
    leave=Leave.objects.get(leave_id=id)
    leave.is_forwarded=False
    leave.forwarded_date=datetime.datetime.now()
    leave.save()
    return redirect("eleave_home")

def director_approve(request,id):
    leave=Leave.objects.get(leave_id=id)
    leave.is_approved=True
    leave.approved_date=datetime.datetime.now()
    leave.save()
    return redirect("eleave_home")

def director_reject(request,id):
    leave=Leave.objects.get(leave_id=id)
    leave.is_approved=False
    leave.approved_date=datetime.datetime.now()
    leave.save()
    return redirect("eleave_home")
