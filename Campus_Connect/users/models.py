from django.db import models
from django.contrib.auth.models import User


class tags(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name


class profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    Name = models.CharField(max_length=300)
    tags=models.ManyToManyField('tags', blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    link=models.CharField(max_length=2000, null=True, blank=True)
    college=models.CharField(max_length=1000, blank=True, null=True)
    def __str__(self) :
        return str(self.user)
    


class blog(models.Model):
    user=models.ManyToManyField(User,  blank=True, null=True)
    tags=models.ForeignKey('tags', blank=True, null=True , on_delete=models.CASCADE)
    title=models.CharField(max_length=200, null=True, blank=True)
    all=models.TextField(blank=True, null=True)
    def __str__(self):
        return self.title