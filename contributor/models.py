from django.db import models
from general.models import NormalUser,Contributor
# Create your models here.
class Job(models.Model):
    companyPicture=models.FileField(upload_to ='images/',null=True, blank=True)
    jobTitle=models.CharField(max_length=30,null=True, blank=True)
    companyName=models.CharField(max_length=30,null=True, blank=True)
    jobSalary=models.CharField(max_length=30,null=True, blank=True)
    jobDescription=models.CharField(max_length=10000,null=True, blank=True)
    contributor=models.ForeignKey(Contributor, on_delete=models.CASCADE)

class Course(models.Model):
    courseTitle=models.CharField(max_length=30,null=True, blank=True)
    companyName=models.CharField(max_length=30,null=True, blank=True)
    courseDescription=models.CharField(max_length=10000,null=True, blank=True)
    contributor=models.ForeignKey(Contributor, on_delete=models.CASCADE)

class Article(models.Model):
    articleTitle=models.CharField(max_length=30,null=True, blank=True)
    articleDescription=models.CharField(max_length=10000,null=True, blank=True)
    contributor=models.ForeignKey(Contributor, on_delete=models.CASCADE)

class JobApplicationDetails(models.Model):
    userApplied=models.ForeignKey(NormalUser, on_delete=models.CASCADE)
    jobApplied=models.ForeignKey(Job,on_delete=models.CASCADE)
    jobTitle=models.CharField(max_length=30,null=True, blank=True)
    companyName=models.CharField(max_length=30,null=True, blank=True)
    userName=models.CharField(max_length=30,null=True, blank=True)
    realName=models.CharField(max_length=30,null=True, blank=True)
    age=models.IntegerField()
    resume=models.FileField(upload_to ='resumes/',null=True, blank=True)
    class Meta:
        unique_together=["userApplied","jobApplied"]

class CourseApplicationDetails(models.Model):
    userApplied=models.ForeignKey(NormalUser, on_delete=models.CASCADE)
    courseApplied=models.ForeignKey(Course,on_delete=models.CASCADE)
    courseTitle=models.CharField(max_length=30,null=True, blank=True)
    companyName=models.CharField(max_length=30,null=True, blank=True)
    userName=models.CharField(max_length=30,null=True, blank=True)
    realName=models.CharField(max_length=30,null=True, blank=True)
    age=models.IntegerField()
    startDate=models.CharField(max_length=30,null=True, blank=True)
    class Meta:
        unique_together=["userApplied","courseApplied"]
