from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from . models import Profile,Blog


# default user profile form
class userform(UserCreationForm):
  class Meta:
    model = User
    fields = ['username', 'first_name', 'last_name','email','password1', 'password2']
    labels = {'email': 'Email'}

# removing radio buttom of password based authentication
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    if 'usable_password' in self.fields:
        del self.fields['usable_password'] 


# extra field in default user
class profileform(forms.ModelForm):
  class Meta:
    model = Profile
    fields = ['mobile_no', 'address','dob','profile_pic']
    widgets = {  
            'dob': forms.DateInput(attrs={'type': 'date'}),
            
        }

class blogform(forms.ModelForm):
  class Meta:
    model = Blog
    fields = ['title', 'description']
  
# update user

class edituser(UserChangeForm):
  password = None
  class Meta:
    model = User
    fields = ['username', 'first_name', 'last_name','email']
