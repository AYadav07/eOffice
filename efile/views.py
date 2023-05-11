from django.shortcuts import render,redirect
import datetime
from django.db.models import Q
from accounts.models import Department,Account ,Director
from eLeave.models import Leave
from efile.forms import UploadDoc,SendFile
from .models import File,Docs,FileAction,DocAction

# Create your views here.

def efile_home(request):
    if Director.objects.filter(director__user_id=request.user.user_id):
        files=File.objects.filter(created_by=request.user)
        pending_files=File.objects.filter(file_access=request.user)
        completed_files=FileAction.objects.filter(Q(receiver=request.user) & Q(is_opened=True))
        return render(request,'efile/home.html',{'files':files,'pending_files':pending_files,'completed_files':completed_files})

    elif Department.objects.filter(dept_HOD__user_id=request.user.user_id).exists():
        files=File.objects.filter(created_by=request.user)
        pending_files=File.objects.filter(file_access=request.user)
        completed_files=FileAction.objects.filter(Q(receiver=request.user) & Q(is_opened=True))
        return render(request,'efile/home.html',{'files':files,'pending_files':pending_files,'completed_files':completed_files})

    else:
        files=File.objects.filter(created_by=request.user)
        pending_files=File.objects.filter(file_access=request.user)
        completed_files=FileAction.objects.filter(Q(receiver=request.user) & Q(is_opened=True))
        return render(request,'efile/home.html',{'files':files,'pending_files':pending_files,'completed_files':completed_files})

    return render(request,'pims/personal_detail.html',{'account':account, 'detail':detail,'creator':creator})



def createfile(request):
    if request.method =='POST':
        created_by=request.user
        file_name=request.POST['file_name']
        description=request.POST['description']
        file_access=request.user


        new_file= File(created_by=created_by,file_name=file_name,file_description=description,file_access=file_access)
        new_file.save()
        file=File.objects.get(file_id=new_file.file_id)
        file_id=file
        receiver=request.user
        sender=request.user
        comment="New file is created"
        fileaction=FileAction(file_id=file_id,receiver=receiver,sender=sender,comment=comment)
        fileaction.save()

        

        return redirect('efile_home')

    return render(request,'efile/createfile.html')

def open_file(request,id):
    file=File.objects.get(file_id=id)
    fileactions=FileAction.objects.filter(file_id__file_id=id)
    docs=Docs.objects.filter(file__file_id=id)
    return render(request,'efile/file.html',{'docs':docs,'file':file,'fileactions':fileactions})



def uploadfile(request,id):
    file=File.objects.get(file_id=id)
    if request.method == "POST":
        form=UploadDoc(request.POST,request.FILES)
        if form.is_valid():
            new_form=form.save(commit=False)
            new_form.file=file
            new_form.uploaded_by=request.user
            new_form.save()
            docs=Docs.objects.filter(file__file_id=id)
            return render(request,'efile/file.html',{'docs':docs,'file':file})
    form=UploadDoc()
    return render(request,'efile/uploaddoc.html',{'form':form})


def sendfile(request,id):
    file=File.objects.get(file_id=id)
    fileaction=FileAction.objects.get(Q(file_id=file) & Q(is_opened=False))
    if request.method == "POST":
        form=SendFile(request.POST)
        if form.is_valid():
            fileaction.is_opened=True
            fileaction.save()
            new_form=form.save(commit=False)
            new_form.file_id=file
            new_form.sender=request.user
            new_form.uploaded_by=request.user
            new_form.save()
            file.file_access=new_form.receiver
            file.save()
            return redirect('efile_home')
    form=SendFile()
    return render(request,'efile/sendfile.html',{'form':form})


def opendoc(request,id):
    docs=Docs.objects.get(doc_id=id)
    docactions=DocAction.objects.filter(doc_id__doc_id=id)
    return render(request,'efile/doc.html',{'docs':docs,'docactions':docactions})

