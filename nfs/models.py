from django.db import models
from autoslug import AutoSlugField
from django.utils.html import format_html
from ckeditor.fields import RichTextField
from django_ckeditor_5.fields import CKEditor5Field
from tinymce import models as tinymce_models
import datetime

from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# from django.contrib.auth import get_user_model

# User = get_user_model()

# Create your models here


class Enquiry(models.Model):
    Name_nfs=models.CharField(max_length=50)
    Email_nfs=models.EmailField(max_length=254, unique=True)
    Message_nfs=models.TextField()
    def __str__(self):
        return self.Name_nfs


class Admit_Card(models.Model):
    Post_Title = models.CharField(max_length=100, null=True)
    Post_Name = models.CharField(max_length=100, null=True)
    Post_Date = models.DateTimeField(null=True)
    Short_Info = models.TextField(max_length=1000, null=True)
    Discription = RichTextField(null=True)
    # link= models.URLField(null=True)

    slug = AutoSlugField(populate_from="Post_Name", unique=True,null=True,default=None)

    def __str__(self):
        return self.Post_Title   
class Govt_Scheme(models.Model):
    Post_Title = models.CharField(max_length=100, null=True)
    Post_Name = models.CharField(max_length=100, null=True)
    Post_Date = models.DateTimeField(null=True)
    Short_Info = models.TextField(max_length=1000, null=True)
    Discription = RichTextField(null=True)
    Payment = models.CharField(max_length=10, null=True)
    ServiceCharge= models.CharField(max_length=10, null= True)
    SupportingDoc= models.TextField(max_length=50, null=True)
    Payment_Link = models.CharField(max_length=50, null=True)

    # link= models.URLField(null=True)

    slug = AutoSlugField(populate_from="Post_Name", unique=True,null=True,default=None)

    def __str__(self):
        return self.Post_Title      
    
class Result(models.Model):
    Post_Title = models.CharField(max_length=100, null=True)
    Post_Name = models.CharField(max_length=100, null=True)
    Post_Date = models.DateTimeField(null=True)
    Short_Info = models.TextField(max_length=1000, null=True)
    Discription = RichTextField(null=True)
    # link= models.URLField(null=True)

    slug = AutoSlugField(populate_from="Post_Name", unique=True,null=True,default=None)

    def __str__(self):
        return self.Post_Title



class Addmision(models.Model):
    Post_Title = models.CharField(max_length=100, null=True)    
    Post_Name = models.CharField(max_length=100, null=True)
    Post_Date = models.DateTimeField(null=True)
    Short_Info = models.TextField(max_length=1000, null=True)
    Discription =RichTextField(null=True)
    Payment = models.CharField(max_length=10, null=True)
    ServiceCharge= models.CharField(max_length=10, null=True)
    SupportingDoc= models.TextField(max_length=50, null=True)
    # link= models.URLField(null=True)

    slug = AutoSlugField(populate_from="Post_Name", unique=True,null=True,default=None)

    def __str__(self):
        return self.Post_Name   


class Latest_job(models.Model):
    Post_Title = models.CharField(max_length=100, null=True)
    Post_Name = models.CharField(max_length=100)
    Post_Date = models.DateTimeField(null=True)
    Short_Info = models.TextField(max_length=1000, null=True)
    Discription = RichTextField(null=True)
    Payment = models.CharField(max_length=10, null=True)
    ServiceCharge= models.CharField(max_length=10, null=True)
    SupportingDoc= models.TextField(max_length=50, null=True)
    Payment_Link = models.CharField(max_length=50, null=True)
    slug = AutoSlugField(populate_from="Post_Name", unique=True,null=True,default=None)

    def __str__(self):
        return self.Post_Title
    
    
class Multi_Post(models.Model):
    Category_Field = [
        ('RTPS', 'RTPS'),
        ('Mutation/Lagaan', 'Mutation/Lagaan'),
        ('Scholarship', 'Scholarship'),
        ('Anudan', 'Anudan'),
        ('Passport/DL', 'Passport/DL'),
        ('Farmers', 'Farmers'),
        ('Pan Card', 'Pan Card'),
    ]
    Post_Title = models.CharField(max_length=100, null=True)
    Post_Name = models.CharField(max_length=100, null=True)
    Post_Date = models.DateTimeField(null=True)
    Short_Info = models.TextField(max_length=1000, null=True)
    Discription = RichTextField(null=True)
    # link= models.URLField(null=True)
    Category= models.CharField(
        max_length=15,
        choices=Category_Field,
        default='RTPS',
    )

    slug = AutoSlugField(populate_from="Post_Name", unique=True,null=True,default=None)
    Payment = models.CharField(max_length=10, null=True)
    ServiceCharge= models.CharField(max_length=10, null=True)
    SupportingDoc= models.TextField(max_length=50, null=True)
    def __str__(self):
        return self.Post_Title
    

    

    

class incentive(models.Model):
    Post_Name = models.CharField(max_length=100, null=True)
    Post_Date = models.DateTimeField(null=True)
    Short_Info = models.TextField(max_length=1000, null=True)
    Discription = RichTextField(null=True)
    link= models.URLField(null=True)
    Payment = models.CharField(max_length=10, null=True)
    ServiceCharge= models.CharField(max_length=10, null=True)
    SupportingDoc= models.TextField(max_length=50, null=True)
    slug = AutoSlugField(populate_from="Post_Name", unique=True,null=True,default=None)

    def __str__(self):
        return self.Post_Name 
    

class Application(models.Model):
    Applicant_Name = models.CharField(max_length=50, null=True)
    Mobile = models.CharField(max_length=50, null=True)
    Dist_Admin = [
        ('Gopalganj', 'Gopalganj'),
        ('Siwan', 'Siwan'),
        ('Patna', 'Patna'),
        ('Champaran', 'Champaran'),
        ('Motihari', 'Motihari'),
        ('Chhapra', 'Chhapra'),
        ('Aurangabad', 'Aurangabad'),
        ('Gaya', 'Gaya'),
        ('Sasaram', 'Sasaram'),
    ]
    District = models.CharField(max_length=50, null=True)
    State = models.CharField(max_length=10, null=True)
    Form_Type= models.CharField(max_length=50, null=True)
    Target_Url = models.CharField(max_length=1000,null=True)
    Is_Done= models.BooleanField(default=False, null=True)
    Created_At= models.DateTimeField(auto_now=True)
    Payment_Recieved = models.BooleanField(default=False, null=True)
    Amount = models.CharField(max_length=50, null=True)
    Payment_Mode= models.CharField(max_length=50, null=True)    
    Transaction_id= models.CharField(max_length=50, null=True)
    Initiated = models.BooleanField(default=False)
    Completed = models.BooleanField(default=False)
    Remarks = models.TextField(blank=True, null=True)
    Assign_To = models.CharField(
        max_length=15,
        choices=Dist_Admin,
        default='Gopalganj',
    )
    Payment = models.CharField(max_length=10, null=True)
    ServiceCharge= models.CharField(max_length=10, null=True)
    SupportingDoc= models.TextField(max_length=50, null=True)

    def __str__(self):
        return self.Applicant_Name
    def clickable_url(self):
        return format_html('<a href="{0}"target="_blank">Form Url</a>', self.Target_Url)
    
    # clickable_url.short_description = 'Target URL'

    # @property
    # def Target_Url(self):
    #     return "url"

class Partner_Registration(models.Model):
    Name = models.CharField(max_length=20)
    Father= models.CharField(max_length=20)
    State = models.CharField(max_length=20)
    District= models.CharField(max_length=30)
    Address= models.CharField(max_length=60)
    Mobile = models.CharField(max_length=10)
    Email= models.CharField(max_length=40)
    Remark=models.TextField(max_length=100, null=True)

    def __str__(self):
        return self.Name







from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    Dist_Admin = [
       ('Gopalganj', 'Gopalganj'),
        ('Siwan', 'Siwan'),
        ('Patna', 'Patna'),
        ('Champaran', 'Champaran'),
        ('Motihari', 'Motihari'),
        ('Chhapra', 'Chhapra'),
        ('Aurangabad', 'Aurangabad'),
        ('Gaya', 'Gaya'),
        ('Sasaram', 'Sasaram'),
    ]
    email = models.EmailField(unique=True)
    phone_number = models.CharField(unique=True, max_length=10)
    State = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    Assign_To = models.CharField(
        max_length=15,
        choices=Dist_Admin,
        default='Gopalganj',
        )
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class WhatsAppMessage(models.Model):
    from_number = models.CharField(max_length=20)
    message_body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.from_number} at {self.timestamp}"

