from pyexpat import model
from django.core.exceptions import ValidationError
from django import forms
from django.forms import HiddenInput
from django.forms.models import ModelForm

from accounts.models import Account
from .models import File,Docs,FileAction,DocAction


class UploadDoc(ModelForm):
    class Meta:
        model=Docs
        fields=['doc_name','doc_description','comment','doc']


class SendFile(ModelForm):
    receiver=forms.ModelChoiceField(queryset=Account.objects.all())
    class Meta:
        model=FileAction
        fields=['receiver','comment']