# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)  # Hashing password
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("role", "admin")
        return self.create_user(email, password, **extra_fields)
    
class Users(AbstractBaseUser):
    user_id = models.BigAutoField(db_column='User_ID', primary_key=True)
    email = models.EmailField(db_column='Email', unique=True, max_length=255)
    full_name = models.CharField(db_column='Full_Name', max_length=255)
    registration_date = models.DateTimeField(db_column='Registration_Date', auto_now_add=True)
    last_login_date = models.DateTimeField(db_column='Last_Login_Date', blank=True, null=True)
    status = models.CharField(db_column='Status', max_length=50, default="active")
    role = models.CharField(db_column='Role', max_length=50, default="user")

    objects = UserManager()

    USERNAME_FIELD = 'email'  # Login using email
    REQUIRED_FIELDS = ['full_name']

    class Meta:
        db_table = 'Users'


class Department(models.Model):
    dnumber = models.IntegerField(blank=True, null=True)
    dname = models.CharField(max_length=15, blank=True, null=True)
    mgr_ssn = models.CharField(max_length=9, blank=True, null=True)
    mgr_start_date = models.DateField(blank=True, null=True)

    class Meta:
        #managed = #False
        db_table = 'department'


class Employee(models.Model):
    fname = models.CharField(max_length=8, blank=True, null=True)
    minit = models.CharField(max_length=2, blank=True, null=True)
    lname = models.CharField(max_length=8, blank=True, null=True)
    ssn = models.CharField(primary_key=True, max_length=9)
    bdate = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=27, blank=True, null=True)
    sex = models.CharField(max_length=1, blank=True, null=True)
    salary = models.IntegerField()
    super_ssn = models.CharField(max_length=9, blank=True, null=True)
    dno = models.IntegerField()

    class Meta:
        #managed = #False
        db_table = 'employee'
