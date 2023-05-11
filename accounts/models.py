from unicodedata import name
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager



'''def get_profie_image_filepath(self, filename):
    return f'profile_images/{self.pk}/{"profile_image.png"}'''

class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must have a email address")

        if not username:
            raise ValueError("Users must have a username")
        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Department(models.Model):
    dept_id         =models.BigAutoField(unique=True, primary_key=True)
    dept_name       =models.CharField(max_length=50, unique=True)
    dept_HOD        =models.ForeignKey('Account',related_name='Account',null=True,blank=True,on_delete=models.CASCADE)
    def __str__(self):
        return self.dept_name



class Account(AbstractBaseUser):
    '''POR_CHOICE      =(
        ('D','Director'),
        ('H','HOD'),
        ('S','Staff'),
    )'''
    user_id         =models.BigAutoField(unique=True, primary_key=True)
    email           =models.EmailField(verbose_name='email',help_text='Email',max_length=60, unique=True)
    username        =models.CharField(max_length=30,unique=True)
    first_name      =models.CharField(max_length=30)
    last_name       =models.CharField(max_length=30)
    department      =models.ForeignKey(Department,null=True,blank=True,on_delete=models.CASCADE)
    #por             =models.CharField(max_length=1,choices=POR_CHOICE)
    date_joined     =models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login      =models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin        =models.BooleanField(default=False)
    is_active       =models.BooleanField(default=True)
    is_staff        =models.BooleanField(default=False)
    is_superuser    =models.BooleanField(default=False)
    profile_image   =models.ImageField(upload_to='profile_pics', blank=True, default='default.jpg')
    
    objects = MyAccountManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True





'''class PositionOfResponsibility(models.Model):
    por_id         =models.BigAutoField(unique=True, primary_key=True)
    por_name       =models.CharField(max_length=30)'''

class Director(models.Model):
    id              =models.BigAutoField(unique=True, primary_key=True)
    #name            =models.TextChoices('Director')
    director        =models.ForeignKey('Account',null=True,blank=True,on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.director.is_admin=True
        self.director.is_staff=True
        self.director.is_superuser=True
        self.director.save()

    def __str__(self):
        return self.director.username

class Creator(models.Model):
    id              =models.BigAutoField(unique=True, primary_key=True)
    #name            =models.TextChoices('Director')
    creator        =models.ForeignKey('Account',null=True,blank=True,on_delete=models.CASCADE)

    '''def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.director.save()'''

    def __str__(self):
        return self.creator.username