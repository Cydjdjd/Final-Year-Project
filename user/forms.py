from django import forms
from general.models import User
class jobApplyForm(forms.Form):
    jobTitle=forms.CharField(label='Job Title',widget = forms.TextInput(attrs={'readonly':'readonly'}))
    companyName=forms.CharField(label='Company',widget = forms.TextInput(attrs={'readonly':'readonly'}))
    userName=forms.CharField(label='Username',max_length=30)
    realName=forms.CharField(label='Real Name',max_length=30)
    age=forms.IntegerField(label='Age',widget = forms.TextInput(attrs={'readonly':'readonly'}))
    resume=forms.FileField(label='Resume', required=True)

class courseApplyForm(forms.Form):
    courseTitle=forms.CharField(label='Course Title',widget = forms.TextInput(attrs={'readonly':'readonly'}))
    companyName=forms.CharField(label='Company',widget = forms.TextInput(attrs={'readonly':'readonly'}))
    userName=forms.CharField(label='Username',max_length=30)
    realName=forms.CharField(label='Real Name',max_length=30)
    age=forms.IntegerField(label='Age',widget = forms.TextInput(attrs={'readonly':'readonly'}))
    startDate=forms.CharField(label='Start Date',max_length=30)

class careerCoachingForm(forms.Form):
    realName=forms.CharField(label='Real Name',max_length=30)
    emailAddress=forms.CharField(label='Email Address',max_length=30)
    contactNumber=forms.CharField(label='Contact Number',max_length=30)

class NormalUserProfilePageForm(forms.ModelForm):
    age=forms.IntegerField()
    ic=forms.FileField()
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
       model = User
       fields = ('username','password','age','ic');