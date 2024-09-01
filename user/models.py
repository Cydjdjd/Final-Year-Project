from django.db import models
from general.models import NormalUser
# Create your models here.
class careerCoachingApplicationDetails(models.Model):
    realName=models.CharField(max_length=30,null=True, blank=True)
    emailAddress=models.CharField(max_length=30,null=True, blank=True)
    contactNumber=models.CharField(max_length=30,null=True, blank=True)
    normalUserApplied=models.ForeignKey(NormalUser, on_delete=models.CASCADE)