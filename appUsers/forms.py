from django import forms
from django.contrib.auth.models import User
from appUsers.models import userProfile
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):

    email = forms.EmailField()
    
    class Meta():
        model = User
        fields = ('username','first_name', 'last_name',
                  'email', 'password1', 'password2')

        label = {'password1': 'Password',
                 'password2': 'Confirm password'}


class UserProfileForm(forms.ModelForm):

    bio = forms.CharField(required=False)
    student = 'student'
    userTypes = [(student, 'student')]

    userType = forms.ChoiceField(required=True, choices=userTypes)

    class Meta():
        model = userProfile
        fields = ('bio', 'userType')
