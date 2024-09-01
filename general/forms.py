from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from general.models import NormalUser,Contributor,User

class NormalSignUpForm(UserCreationForm):
    age=forms.IntegerField()
    ic=forms.FileField()
    class Meta(UserCreationForm.Meta):
        model = User
        fields=UserCreationForm.Meta.fields+('age','ic');
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.is_normal = True
        user.save()
        age=self.cleaned_data.get('age')
        ic=self.cleaned_data.get('ic')
        Normaluser = NormalUser.objects.create(user=user,age=age,ic=ic)
        return user

class NormalLoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=30)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

class ContributorSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields=('username','password1','password2')
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.is_contributor = True
        user.save()
        contributor= Contributor.objects.create(user=user)
        return user

class ContributorLoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=30)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)