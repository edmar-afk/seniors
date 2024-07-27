from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.utils import timezone
# Create your models here.


class Profile(models.Model):
    name = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = models.FileField(upload_to='media/', validators=[FileExtensionValidator(allowed_extensions=['png', 'jpeg', 'jpg'])],)
    phone_num = models.CharField(max_length=250)
    dob = models.CharField(max_length=250)
    purok = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    barangay = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=250)
    
    def __str__(self):
        return self.user.username
    

class Event(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    date_held = models.DateTimeField()
    likes = models.ManyToManyField(User, blank=True, null=True)
    


class SeniorResponse(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    date_submitted = models.DateTimeField()