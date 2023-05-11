
from django.db import models
from accounts.models import Account

# Create your models here.
class Leave(models.Model):
    leave_id         =models.BigAutoField(unique=True, primary_key=True)
    user_id          =models.ForeignKey(Account,null=True,on_delete=models.CASCADE,editable=False)
    #dept             =models.ForeignKey(Department,null=True,on_delete=models.CASCADE,editable=False)
    start_date       =models.DateField(null=True)
    end_date         =models.DateField(null=True)
    reason           =models.CharField(max_length=300)
    is_forwarded     =models.BooleanField(null=True,blank=True)
    is_approved      =models.BooleanField(null=True,blank=True)
    description      =models.CharField(max_length=300, null=True)
    applied_date     =models.DateTimeField(auto_now_add=True,null=True)
    forwarded_date   =models.DateTimeField(null=True)
    approved_date    =models.DateTimeField(null=True)