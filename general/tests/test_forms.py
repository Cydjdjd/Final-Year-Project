import os
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from general.models import User,NormalUser,Contributor
from general.forms import NormalSignUpForm,NormalLoginForm,ContributorLoginForm,ContributorSignUpForm

class NormalSignUpFormTest(TestCase):
    def test_correct_data_type(self):
        with open('general/tests/images/icImage.jpg', 'rb') as f:
            form=NormalSignUpForm({'username':'BobTan123','password1':'abc123!@#','password2':'abc123!@#', 'age':56},{'ic':SimpleUploadedFile(name="IC",content=f.read())})
            self.assertTrue(form.is_valid())

    def test_username_label(self):
        form=NormalSignUpForm()
        self.assertTrue(form.fields['username'].label is None or form.fields['username'].label == 'Username')

    def test_password_label(self):
        form=NormalSignUpForm()
        self.assertTrue(form.fields['password1'].label is None or form.fields['password1'].label == 'Password')

    def test_age_label(self):
        form=NormalSignUpForm()
        self.assertTrue(form.fields['age'].label is None or form.fields['age'].label == 'Age')

    def test_ic_label(self):
        form=NormalSignUpForm()
        self.assertTrue(form.fields['ic'].label is None or form.fields['ic'].label == 'ic')

class ContributorSignUpFormTest(TestCase):
    def test_correct_data_type(self):
        form=ContributorSignUpForm({'username':'MrBoss','password1':'abc123!@#','password2':'abc123!@#'})
        self.assertTrue(form.is_valid())

    def test_username_label(self):
        form=ContributorSignUpForm()
        self.assertTrue(form.fields['username'].label is None or form.fields['username'].label == 'Username')

    def test_password_label(self):
        form=ContributorSignUpForm()
        self.assertTrue(form.fields['password1'].label is None or form.fields['password1'].label == 'Password')

class NormalLoginFormTest(TestCase):
    def test_correct_data_type(self):
        User.objects.create(username='BobTan123',password='abc123!@#',is_normal=True)
        form=NormalLoginForm({'username':'BobTan123','password':'abc123!@#'})
        self.assertTrue(form.is_valid())

    def test_username_label(self):
        form=NormalLoginForm()
        self.assertTrue(form.fields['username'].label is None or form.fields['username'].label == 'Username')

    def test_password_label(self):
        form=NormalLoginForm()
        self.assertTrue(form.fields['password'].label is None or form.fields['password'].label == 'Password')

class ContributorLoginFormTest(TestCase):
    def test_correct_data_type(self):
        User.objects.create(username="mt123",password="abc123!@#",is_contributor=True)
        form=ContributorLoginForm({'username':'mt123','password':'abc123!@#'})
        self.assertTrue(form.is_valid())

    def test_username_label(self):
        form=ContributorLoginForm()
        self.assertTrue(form.fields['username'].label is None or form.fields['username'].label == 'Username')

    def test_password_label(self):
        form=ContributorLoginForm()
        self.assertTrue(form.fields['password'].label is None or form.fields['password'].label == 'Password')