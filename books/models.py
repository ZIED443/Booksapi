from django.db import models
from django.db.models.deletion import SET_DEFAULT
from django.utils.translation import gettext_lazy as _
import datetime
from datetime import datetime
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class CustomUser(BaseUserManager):

    def create_superuser(self,  password, email, user_name , **other_fields):   
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        
        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(   password, email, user_name , **other_fields)

    def create_user(self,  password, email, user_name , **other_fields):

        
        if not email:
            raise ValueError(_('You need to provide an email adress  '))

       
        user = self.model( password = password  , email = email ,user_name=user_name, **other_fields)
        user.set_password(password)
        user.save()
        return user          
  

class User(AbstractBaseUser, PermissionsMixin):  
     sex  = (
        ('male' , 'male'),
        ('female','female')
       
    )
     is_staff = models.BooleanField(default=False)
     is_active = models.BooleanField(default=True)
     user_name =  models.CharField(max_length=200 , blank=True, null=True)
     email =  models.EmailField(_('email address'),unique=True )
     password =  models.CharField(max_length=200 , null=False)
     sex= models.CharField(choices= sex ,max_length=50,blank=True)  
     objects = CustomUser()   
     USERNAME_FIELD = 'email'
     REQUIRED_FIELDS = ['password']  
     def __str__(self):
        return str(self.email)




class Auhor(models.Model):
   name=models.CharField(max_length=200 , blank=True, null=True)
   birthday = models.DateTimeField(blank=True,null=True,default=datetime.now)

class Book (models.Model): 
    author = models.ForeignKey( Auhor, blank=True,null=True,   on_delete=SET_DEFAULT,  default=None)
    date_release = models.DateTimeField(blank=True,null=True,default=datetime.now)
    name=models.CharField(max_length=200 , blank=True, null=True)


class Bookreservation: 
    user = models.ForeignKey( User, blank=True,null=True,   on_delete=SET_DEFAULT,  default=None)
    book = models.ForeignKey( Book, blank=True,null=True,   on_delete=SET_DEFAULT,  default=None)
    date1 = models.DateTimeField(blank=True,null=True,default=datetime.now)
    date2 = models.DateTimeField(blank=True,null=True,default=datetime.now)


 
    