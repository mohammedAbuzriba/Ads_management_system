from django.db import models
from django.contrib.auth.models import User
from django.utils.text import Truncator
from setuptools.command.upload import upload
from ckeditor.fields import RichTextField
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)


class Section(models.Model):
    name = models.CharField(max_length=50,unique=True)
    name_ar = models.CharField(default='section',max_length=50)
    description = models.CharField(max_length=150)
    description_ar = models.CharField(default='section',max_length=150)
    img = models.ImageField(null=True,blank=True,upload_to='static/img')
    def __str__(self):
        return self.name

class Ads(models.Model):
    subject = models.CharField(max_length=255)
    messageAds = RichTextField(null=True)
    #messageAds = models.TextField(null=True,max_length=4000)
    section = models.ForeignKey(Section,related_name='ads',on_delete=models.CASCADE)
    created_by = models.ForeignKey(User,related_name='ads',on_delete=models.CASCADE)
    created_dt = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(null=True,blank=True,upload_to='static/img')
    views = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=False)
    Archives = models.BooleanField(default=False)
    updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete=models.CASCADE)
    updated_dt = models.DateTimeField(null=True)

    def __str__(self):
        return self.subject



class Comments(models.Model):
    message = models.TextField(max_length=4000)
    ads = models.ForeignKey(Ads,related_name='comments',on_delete=models.CASCADE)
    created_by = models.ForeignKey(User,related_name='comments',on_delete=models.CASCADE)
    created_dt = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(User,null=True,related_name='+',on_delete=models.CASCADE)
    updated_dt = models.DateTimeField(null=True)

    # def __str__(self):
    #     truncatedMessage = Truncator(self.message)
    #     return self.truncatedMessage.chars(30)




class Archives(models.Model):
    ads = models.ForeignKey(Ads, related_name='archivetest', on_delete=models.CASCADE)
    save_by = models.ForeignKey(User, related_name='archive', on_delete=models.CASCADE)
    save_dt = models.DateTimeField(auto_now_add=True)