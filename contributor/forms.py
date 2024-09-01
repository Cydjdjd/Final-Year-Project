from django import forms 
from general.models import User
class jobsCreate(forms.Form):
    companyPicture=forms.FileField(label='Company Picture', required=True)
    jobTitle=forms.CharField(label='Job Title',max_length=30)
    companyName=forms.CharField(label="Company Name",max_length=30)
    jobSalary=forms.CharField(label="Job Salary",max_length=30)
    jobDescription=forms.CharField(label="Job Description",widget=forms.Textarea(attrs={"rows":"5"}))

class courseCreate(forms.Form):
    courseTitle=forms.CharField(label='Course Title',max_length=30)
    companyName=forms.CharField(label="Company Name",max_length=30)
    courseDescription=forms.CharField(label="Course Description",widget=forms.Textarea(attrs={"rows":"5"}))

class articleCreate(forms.Form):
    articleTitle=forms.CharField(label='Article Title',max_length=30)
    articleDescription=forms.CharField(label="Article Description",widget=forms.Textarea(attrs={"rows":"5"}))

class ContributorProfilePageForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
       model = User
       fields = ('username','password')