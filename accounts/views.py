import email
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import authenticate,logout,login

from accounts.models import Account, Department, Director
from .forms import AccountAuthenticationForm,AccountEditForm


'''def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']


        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            print("Logged in")
            return render(request,'postlogin.html')

        else:
            messages.info(request,'Invalid Credentials')

    else:
        return render(request,'login1.html')'''


def login_view(request):
    context={}

    user=request.user
    if user.is_authenticated:
        return render(request,'account/postlogin.html')

    if request.POST:
        form= AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email=request.POST['email']
            password=request.POST['password']
            user=authenticate(email=email,password=password)
            if user:
                login(request,user)
                return render(request,'account/postlogin.html')

    else:
        form=AccountAuthenticationForm()

    context['login_form']=form
    return render(request,'account/login1.html',context)
                



def efile(request):
    return render(request,'eFile.html')


def kms(request):
    return render(request,'eFile.html')


def eleave(request):
    return render(request,'eFile.html')


def pims(request):
    return render(request,'pims.html')

    

# Create your views here.iojoi

def logout_view(request):
    logout(request)
    return redirect("login")


def profile_view(request):
    priority=0
    acccount=Account.objects.get(user_id=request.user.user_id)
    if Director.objects.filter(director__user_id=request.user.user_id).exists():
        priority=1
    elif Department.objects.filter(dept_HOD__user_id=request.user.user_id).exists():
        priority=2
    return render(request,'account/profile_view.html',{'account':acccount,'priority':priority})


def profile_edit(request):
    instance=Account.objects.get(user_id=request.user.user_id)
    form=AccountEditForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect("login") 
    return render(request,'account/profile_edit.html',{'form':form})
    form_class=AccountEditForm
