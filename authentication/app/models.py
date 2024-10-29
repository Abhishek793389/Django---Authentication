from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  mobile_no = models.CharField(max_length=11, blank=False, unique=True)
  address = models.CharField(max_length=100)
  dob = models.DateField()
  profile_pic = models.ImageField(upload_to='profile',blank=True, null=True)



class Blog(models.Model):
  user = models.ForeignKey(User, on_delete = models.CASCADE)
  title = models.CharField(max_length=200)
  description = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True) 