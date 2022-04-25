from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Section(models.Model):
    name = models.CharField(max_length=50,unique=True)
    description = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Ads(models.Model):
    subject = models.CharField(max_length=255)
    section = models.ForeignKey(Section,related_name='ads',on_delete=models.CASCADE)
    created_by = models.ForeignKey(User,related_name='ads',on_delete=models.CASCADE)
    created_dt = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)
    updated_by = models.ForeignKey(User,null=True,related_name='+',on_delete=models.CASCADE)
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
