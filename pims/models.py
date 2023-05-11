from django.db import models
from accounts.models import Account
import hashlib, random, sys
from . import stage


def create_session_hash():
  hash = hashlib.sha1()
  hash.update(str(random.randint(0,sys.maxsize)).encode('utf-8'))
  return hash.hexdigest()



# Create your models here.
'''GENDER_CHOICE      =(
        ('Male','Male'),
        ('Female','Female'),
        ('Other','Other'),
    )

BLOOD_CHOICE    =(
    ('A+','A+'),
    ('A-','A-'),
    ('B+','B+'),
    ('B-','B-'),
    ('O+','O+'),
    ('O-','O-'),
    ('AB+','AB+'),
    ('AB-','AB-'),
)

CATEGORY_CHOICE =(
    ('GEN','Genral'),
    ('OBC','OBC'),
    ('SC','SC'),
    ('ST','ST'),
    ('PWD','PwD'),
)

MARITAL_CHOICE  =(
    ('MARRIED','Married'),
    ('UNMARRIED','Unmarried'),
    ('DIVORCED','Divorced'),
)'''

class Pims(models.Model):
    pims_id         =models.BigAutoField(unique=True, primary_key=True)
    session_hash = models.CharField(max_length=40, unique=True)
    stage = models.CharField(max_length=10, default=stage.STAGE_1, null=True)
    user_id          =models.OneToOneField(Account,on_delete=models.CASCADE)

    # STAGE 1

    father_name      =models.CharField(max_length=50,verbose_name="Father Name",blank=True)
    mother_name      =models.CharField(max_length=50,verbose_name="Mother Name",blank=True)
    aadhar_no        =models.PositiveBigIntegerField(unique=True,blank=True)
    dob             =models.DateField(blank=True)
    gender          =models.CharField(max_length=10,blank=True)
    category        =models.CharField(max_length=10,blank=True)
    religion        =models.CharField(max_length=20,blank=True)
    country         =models.CharField(max_length=20,blank=True)
    blood_group     =models.CharField(max_length=10,blank=True)
    mother_tongue   =models.CharField(max_length=20,blank=True)
    marital_status  =models.CharField(max_length=20,blank=True)
    join_date       =models.DateField(blank=True,null=True)
    #appointment photograph
    #scanned signature
    
    # STAGE 2

    degree              =models.CharField(max_length=50,blank=True)
    institute           =models.CharField(max_length=100,blank=True)
    discipline          =models.CharField(max_length=100,blank=True)
    passing_grade       =models.CharField(max_length=10,blank=True)
    passing_percentage  =models.FloatField(blank=True,null=True)
    passing_year        =models.DateField(blank=True,null=True)
    degree_type         =models.CharField(max_length=20,blank=True)
    course_coordinator  =models.CharField(max_length=50,blank=True)
    organisation        =models.CharField(max_length=100,blank=True)
    course_name         =models.CharField(max_length=100,blank=True)
    org_address         =models.CharField(max_length=100,blank=True)
    org_city            =models.CharField(max_length=50,blank=True)
    org_country         =models.CharField(max_length=50,blank=True)
    org_state           =models.CharField(max_length=50,blank=True)
    org_district        =models.CharField(max_length=50,blank=True)
    course_start_date   =models.DateField(blank=True,null=True)
    course_end_date     =models.DateField(blank=True,null=True)
    is_course_completed =models.BooleanField(blank=True,default=True, null=True)
    course_grade        =models.CharField(max_length=10,blank=True)

    # STAGE 3

    address         =models.CharField(max_length=200,blank=True)
    city            =models.CharField(max_length=50,blank=True)
    district        =models.CharField(max_length=50,blank=True)
    state           =models.CharField(max_length=50,blank=True)
    post_office     =models.CharField(max_length=50,blank=True)
    pincode         =models.PositiveSmallIntegerField(blank=True,null=True)
    mobile          =models.BigIntegerField(blank=True,null=True)
    curr_address         =models.CharField(max_length=200,blank=True)
    curr_city            =models.CharField(max_length=50,blank=True)
    curr_district        =models.CharField(max_length=50,blank=True)
    curr_state           =models.CharField(max_length=50,blank=True)
    curr_post_office     =models.CharField(max_length=50,blank=True)
    curr_pincode         =models.PositiveSmallIntegerField(blank=True,null=True)
    director_verified    =models.BooleanField(blank=True,default=False, null=True)
    user_feedback       =models.TextField(blank=True,null=True)



    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.session_hash:
            while True:
                session_hash = create_session_hash()
                if Pims.objects.filter(session_hash=session_hash).count() == 0:
                    self.session_hash = session_hash
                    break

    '''@staticmethod
    def get_fields_by_stage(stage):
        fields = ['stage']  # Must always be present
        if stage == forms.STAGE_1:
            fields.extend(['father_name', 'mother_name','aadhar_no','dob','gender','category','religion',
            'blood_group','mother_tongue','marital_status','join_date'])
        elif stage == forms.STAGE_2:
            fields.extend(['degree','institute','discipline','passing_grade','passing_percentage','passing_year',
            'degree_type','course_coordinator','organisation','course_name','org_address','org_city','org_country',
            'org_state','org_district','course_start_date','course_end_date','is_course_completed','course_grade'])
        elif stage == forms.STAGE_3:
            fields.extend(['address','city','district','state','post_office','pincode','mobile',
            'curr_address','curr_city','curr_district','curr_state','curr_post_office','curr_pincode',' user_feedback'])
        return fields'''



