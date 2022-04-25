from django import forms
from .models import Ads , Comments

class NewAdsForm(forms.ModelForm):

    message = forms.CharField(widget=forms.Textarea(
        attrs={'rows':5,'placeholder':'What is on your mind?'}
    ),
    max_length=4000,
    help_text='The max length of the text is 4000')

    class Meta:
        model = Ads
        fields = ['subject','message']


class CommentsForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ['message',]