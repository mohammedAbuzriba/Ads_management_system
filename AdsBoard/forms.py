import django.utils.translation
from django.utils.translation import gettext_lazy as _
from django import forms
from .models import Ads, Comments, Section, Profile
from ckeditor.fields import RichTextField

class NewAdsForm(forms.ModelForm,):

    # message = forms.CharField(widget=forms.Textarea(
    #     attrs={'rows':5,'placeholder':'What is on your mind?'}
    # ),
    # max_length=4000,
    # help_text='The max length of the text is 4000')
    class Meta:
        model = Ads
        fields = ['subject','messageAds','img']
        labels = {
            'subject': _('subject'),
            'messageAds': _('Message'),
            'img': _('image'),
        }




class CommentsForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ['message',]
        labels = {
            'message': _('Comment'),
        }


class SectionUpdateForm(forms.ModelForm):

    class Meta:
        model = Section
        fields = ['name','name_ar','description','description_ar','img']
        labels = {
            'name': _('Name'),
            'name_ar': _('Name Arabic'),
            'description': _('Description'),
            'description_ar': _('Description Arabic'),
            'img': _('Image'),
        }




class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['bio','birthday','gender','img']

