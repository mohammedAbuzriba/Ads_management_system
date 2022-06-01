from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from AdsBoard.models import Profile


class SignUpForm(UserCreationForm):

    # first_name = forms.CharField(max_length=255,required=True,widget=forms.TextInput())
    # last_name = forms.CharField(max_length=255,required=True,widget=forms.TextInput())
    # email = forms.CharField(max_length=255,required=True,widget=forms.EmailInput())

    class Meta:
        model=User
        fields = ['username','email','password1','password2']
        labels = {
            'username': _('User name'),
            'email': _('Email'),
            'password1': _('password1'),
            'password2': _('password2'),
        }

class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name','last_name','username','email']


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']


class UpdateProfileForm(forms.ModelForm):
    # avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    # bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    # birthday = forms.DateField()
    # gender = forms.CharField(
    #     max_length=6,
    #     choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE')]
    # )
    # img = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))

    class Meta:
        model = Profile
        fields = ['bio','birthday','gender','img']

# class ProfileUpdateForm(forms.ModelForm):
#
#     class Meta:
#         model = Profile
#         fields = ['bio','birthday','gender','img']
