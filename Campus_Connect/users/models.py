from django.db import models
class tags(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name


class profile(models.Model):
    Name = models.CharField(max_length=300)
    description = models.TextField(null=True, blank=True)
    link=models.CharField(max_length=2000, null=True, blank=True)
    college=models.CharField(max_length=1000, blank=True, null=True)
    def __str__(self) :
        return self.college
    
