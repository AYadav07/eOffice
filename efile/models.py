from sys import set_coroutine_origin_tracking_depth
from django.db import models
from accounts.models import Account

# Create your models here.
class File(models.Model):
    file_id             =models.BigAutoField(unique=True, primary_key=True)
    file_name           =models.CharField(max_length=50,verbose_name="File Name",blank=True)
    file_description    =models.CharField(max_length=200,verbose_name="File Description",blank=True)
    created_by          =models.ForeignKey(Account,null=True,on_delete=models.CASCADE,editable=False)
    file_access         =models.ForeignKey(Account,null=True,on_delete=models.CASCADE,related_name='work_by+')
    created_on          =models.DateTimeField(auto_now_add=True,null=True)
    is_open             =models.BooleanField(default=True,blank=True)

    def __str__(self):
        return self.file_name


class Docs(models.Model):
    doc_id             =models.BigAutoField(unique=True, primary_key=True)
    doc                =models.FileField(upload_to='uploads/',null=True,blank=True)
    file               =models.ForeignKey(File,null=True,on_delete=models.CASCADE)
    doc_name           =models.CharField(max_length=50,verbose_name="File Name",blank=True)
    doc_description    =models.CharField(max_length=200,verbose_name="File Description",blank=True)
    uploaded_by        =models.ForeignKey(Account,null=True,on_delete=models.CASCADE,editable=False)
    uploaded_on        =models.DateTimeField(auto_now_add=True,null=True)
    comment            =models.CharField(max_length=300,blank=True,null=True)


    def __str__(self):
        return self.doc_name


class FileAction(models.Model):
    id                  =models.BigAutoField(unique=True, primary_key=True)
    file_id             =models.ForeignKey(File,null=True,on_delete=models.CASCADE)
    receiver            =models.ForeignKey(Account,null=True,on_delete=models.CASCADE,related_name='to+')
    sender              =models.ForeignKey(Account,null=True,on_delete=models.CASCADE,related_name='from+')
    is_opened           =models.BooleanField(default=False,null=True)
    sent_on             =models.DateTimeField(auto_now_add=True,null=True)
    comment            =models.CharField(max_length=300,blank=True,null=True)

    def __str__(self):
        return self.file_id.file_name




class DocAction(models.Model):
    id                  =models.BigAutoField(unique=True, primary_key=True)
    doc_id             =models.ForeignKey(Docs,null=True,on_delete=models.CASCADE)
    receiver            =models.ForeignKey(Account,null=True,on_delete=models.CASCADE,related_name='to+')
    sender              =models.ForeignKey(Account,null=True,on_delete=models.CASCADE,related_name='from+')
    is_opened           =models.BooleanField(default=False,null=True)
    comment            =models.CharField(max_length=300,blank=True,null=True)


    def __str__(self):
        return self.doc_id.doc_name

