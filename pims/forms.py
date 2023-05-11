from dataclasses import fields
from django.core.exceptions import ValidationError
from django.forms import HiddenInput
from django.forms.models import ModelForm

from .models import Pims







class BaseApplicationForm(ModelForm):

    required_css_class = 'required'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        required_fields = self.instance.required_fields
        hidden_fields = self.instance.hidden_fields
        for field in self.fields:
            if field in required_fields:
                self.fields.get(field).required = True
            if field in hidden_fields:
                self.fields.get(field).widget = HiddenInput()

    def clean_first_name(self):
        first_name = self.cleaned_data.get("first_name", "")
        if "e" in first_name:
            raise ValidationError("People with 'e' in their first name need not apply.")
        # else
        return first_name

class EditForm(ModelForm):
    class Meta:
        model=Pims
        fields=['father_name','mother_name','aadhar_no','dob','gender','category','religion',
        'country','mother_tongue','join_date','marital_status','blood_group']

class EditForm_2(ModelForm):
    class Meta:
        model=Pims
        fields=['degree','institute','discipline','passing_grade','passing_percentage','passing_year',
            'degree_type','course_coordinator','organisation','course_name','org_address','org_city','org_country',
            'org_state','org_district','course_start_date','course_end_date','is_course_completed','course_grade']


class EditForm_3(ModelForm):
    class Meta:
        model=Pims
        fields=['address','city','district','state','post_office','pincode','mobile',
            'curr_address','curr_city','curr_district','curr_state','curr_post_office','curr_pincode']