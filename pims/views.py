from django.shortcuts import render
import datetime,pytz
from django.views.generic import FormView, TemplateView
from .forms import BaseApplicationForm, EditForm_2, EditForm_3
from accounts.models import Creator,Account, Department, Director
from pims.models import Pims
from . import forms
from .forms import EditForm
# Create your views here.
def pims_home(request):
    if Creator.objects.filter(creator__user_id=request.user.user_id).exists():
        account = Account.objects.all()
        return render(request,'pims/creator.html',{'accounts':account})
    elif Director.objects.filter(director__user_id=request.user.user_id):
        account = Account.objects.all()
        return render(request,'pims/creator.html',{'accounts':account})

    elif Department.objects.filter(dept_HOD__user_id=request.user.user_id).exists():
        account=Account.objects.filter(department=request.user.department)
        return render(request,'pims/creator.html',{'accounts':account})

    else:
        detail=False
        creator=False
        account=Account.objects.filter(user_id=request.user.user_id)
        if Pims.objects.filter(user_id__user_id=request.user.user_id).exists():
            detail=True
            pims=Pims.objects.get(user_id__user_id=request.user.user_id)
            pims_id=pims.pims_id
            return render(request,'pims/personal_detail.html',{'account':account, 'detail':detail,'creator':creator, 'pims_id':pims_id})
    return render(request,'pims/personal_detail.html',{'account':account, 'detail':detail,'creator':creator})



def pims_details(request,id):
    detail=False
    creator=False
    if Creator.objects.filter(creator__user_id=request.user.user_id).exists():
        creator=True
    account=Account.objects.get(user_id=id)
    if Pims.objects.filter(user_id__user_id=id).exists():
        detail=True
        pims=Pims.objects.get(user_id__user_id=id)
        pims_id=pims.pims_id
        return render(request,'pims/personal_detail.html',{'account':account, 'detail':detail,'creator':creator, 'pims_id':pims_id})
    return render(request,'pims/personal_detail.html',{'account':account, 'detail':detail,'creator':creator})

 

def add_details(request,id):
    saved=False
    if request.method =='POST':
        user=Account.objects.get(user_id=id)
        father_name=request.POST['father_name']
        mother_name=request.POST['mother_name']
        aadhar=request.POST['aadhar_no']
        dob=request.POST['dob']
        category=request.POST['category']
        gender=request.POST['gender']
        religion=request.POST['religion']
        country=request.POST['country']
        mother_tongue=request.POST['mother_tongue']
        join_date=request.POST['join_date']
        marital_status=request.POST['marital_status']
        blood_group=request.POST['blood_group']

        new_leave= Pims(user_id=user,father_name=father_name,mother_name=mother_name,
        aadhar_no=aadhar,dob=dob,gender=gender,category=category,religion=religion,
        country=country,mother_tongue=mother_tongue,join_date=join_date,marital_status=marital_status,blood_group=blood_group)
        new_leave.save()
        pims=Pims.objects.get(user_id=user)
        saved=True
        return render(request,'pims/stage2.html',{'pims':pims,'saved':saved})
    return render(request,'pims/stage1.html',{'id':id,'saved':saved})


def add_details2(request,id):
    saved=False
    if request.method == 'POST':
        pims=Pims.objects.get(pims_id=id)
        pims.degree=request.POST['degree']
        pims.institute=request.POST['institute']
        pims.discipline=request.POST['discipline']
        pims.passing_grade=request.POST['passing_grade']
        pims.passing_percentage=request.POST['passing_percentage']
        pims.passing_year=request.POST['passing_year']
        pims.degree_type=request.POST['degree_type']
        pims.course_coordinator=request.POST['course_coordinator']
        pims.organisation=request.POST['organisation']
        pims.course_name=request.POST['course_name']
        pims.org_address=request.POST['org_address']
        pims.org_city=request.POST['org_city']
        pims.org_country=request.POST['org_country']
        pims.org_state=request.POST['org_state']
        pims.org_district=request.POST['org_district']
        pims.course_start_date=request.POST['course_start_date']
        pims.course_end_date=request.POST['course_end_date']
        #pims.is_course_completed=request.POST['is_course_completed']
        pims.course_grade=request.POST['course_grade']
        pims.save()
        pims=Pims.objects.get(pims_id=id)
        saved=True
        return render(request,'pims/stage3.html',{'pims':pims,'saved':saved})
    return render(request,'pims/stage2.html',{'id':id,'saved':saved})



def add_details3(request,id):
    saved=False
    if request.method == 'POST':
        pims=Pims.objects.get(pims_id=id)
        pims.address=request.POST['address']
        pims.city=request.POST['city']
        pims.district=request.POST['district']
        pims.state=request.POST['state']
        pims.post_office=request.POST['post_office']
        pims.pincode=request.POST['pincode']
        pims.mobile=request.POST['mobile']
        pims.curr_address=request.POST['curr_address']
        pims.curr_city=request.POST['curr_city']
        pims.curr_district=request.POST['curr_district']
        pims.curr_state=request.POST['curr_state']
        pims.curr_pincode=request.POST['curr_pincode']
        pims.save()
        pims=Pims.objects.get(pims_id=id)
        saved=True
        return render(request,'pims/stage3.html',{'pims':pims,'saved':saved})
    return render(request,'pims/stage3.html',{'id':id,'saved':saved})



def edit_1(request,id):
    instance=Pims.objects.get(pims_id=id)
    form=EditForm(request.POST or None, instance=instance)
    if form.is_valid():
        new_form=form.save(commit=False)
        new_form.director_verified=False
        new_form.save()
        return render(request,'pims/view_1.html',{'pims':instance})
    return render(request,'pims/edit.html',{'form':form})


def edit_2(request,id):
    instance=Pims.objects.get(pims_id=id)
    form=EditForm_2(request.POST or None, instance=instance)
    if form.is_valid():
        new_form=form.save(commit=False)
        new_form.director_verified=False
        new_form.save()
        return render(request,'pims/view_2.html',{'pims':instance})
    return render(request,'pims/edit.html',{'form':form})


def edit_3(request,id):
    instance=Pims.objects.get(pims_id=id)
    form=EditForm_3(request.POST or None, instance=instance)
    if form.is_valid():
        new_form=form.save(commit=False)
        new_form.director_verified=False
        new_form.save()
        return render(request,'pims/view_3.html',{'pims':instance})
    return render(request,'pims/edit.html',{'form':form})



def view_1(request,id):
    pims=Pims.objects.get(pims_id=id)
    creator=False
    if Creator.objects.filter(creator__user_id=request.user.user_id).exists():
        creator=True
    director=False
    if Director.objects.filter(director__user_id=request.user.user_id).exists():
        director=True
    return render(request,'pims/view_1.html',{'pims':pims,'creator':creator,'director':director })

def view_2(request,id):
    pims=Pims.objects.get(pims_id=id)
    creator=False
    if Creator.objects.filter(creator__user_id=request.user.user_id).exists():
        creator=True
    director=False
    if Director.objects.filter(director__user_id=request.user.user_id).exists():
        director=True
    return render(request,'pims/view_2.html',{'pims':pims,'creator':creator,'director':director})

def view_3(request,id):
    pims=Pims.objects.get(pims_id=id)
    creator=False
    if Creator.objects.filter(creator__user_id=request.user.user_id).exists():
        creator=True
    director=False
    if Director.objects.filter(director__user_id=request.user.user_id).exists():
        director=True
    return render(request,'pims/view_3.html',{'pims':pims,'director':director,'creator':creator,'director':director})


def director_verify(request,id):
    pims=Pims.objects.get(pims_id=id)
    pims.director_verified=True
    pims.save()
    return render(request,'pims/view_3.html',{'pims':pims})



'''def create_new(request):
    pass'''



'''def get_job_application_from_hash(session_hash):
    # Find and return an unexpired, not-yet-completed Pims
    # with a matching session_hash, or None if no such object exists.
    now = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
    max_age = 300  # Or make this a setting in "settings.py"
    exclude_before = now - datetime.timedelta(seconds=max_age)
    return Pims.objects.filter(
        session_hash=session_hash,
        modified__gte=exclude_before
    ).exclude(
        stage=forms.COMPLETE
    ).first()


class PimsView(FormView):
    template_name = 'pims/add_new.html'
    job_application = None
    form_class = None

    def dispatch(self, request, *args, **kwargs):
        session_hash = request.session.get("session_hash", None)
        # Get the job application for this session. It could be None.
        self.job_application = get_job_application_from_hash(session_hash)
        # Attach the request to "self" so "form_valid()" can access it below.
        self.request = request
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        # This data is valid, so set this form's session hash in the session.
        self.request.session["session_hash"] = form.instance.session_hash
        current_stage = form.cleaned_data.get("stage")
        # Get the next stage after this one.
        new_stage = forms.STAGE_ORDER[forms.STAGE_ORDER.index(current_stage)+1]
        form.instance.stage = new_stage
        form.save()  # This will save the underlying instance.
        if new_stage == forms.COMPLETE:
            return redirect(reverse("job_application:thank_you"))
        # else
        return redirect(reverse("job_application:job_application"))

    def get_form_class(self):
        # If we found a job application that matches the session hash, look at
        # its "stage" attribute to decide which stage of the application we're
        # on. Otherwise assume we're on stage 1.
        stage = self.job_application.stage if self.job_application else forms.STAGE_1
        # Get the form fields appropriate to that stage.
        fields = Pims.get_fields_by_stage(stage)
        # Use those fields to dynamically create a form with "modelform_factory"
        return modelform_factory(Pims, BaseApplicationForm, fields)
    
    def get_form_kwargs(self):
        # Make sure Django uses the same Pims instance we've already been
        # working on. Otherwise it will instantiate a new one after every submit.
        kwargs = super().get_form_kwargs()
        kwargs["instance"] = self.job_application
        return kwargs


class PimsThankYouView(TemplateView):
    template_name = 'pims/thank_you.html'
'''