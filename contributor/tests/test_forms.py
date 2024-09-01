import os
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from Final_Project_Website import settings
from contributor.forms import jobsCreate,courseCreate,articleCreate,ContributorProfilePageForm

class jobsCreateTest(TestCase):
    def test_companyPicture_label(self):
        form=jobsCreate()
        self.assertTrue(form.fields['companyPicture'].label is None or form.fields['companyPicture'].label == 'Company Picture')

    def test_correct_data_type(self):
        with open('contributor/tests/images/google.jpg', 'rb') as f:
            form=jobsCreate({'jobTitle':'IT Support','companyName':'Computer Support Company','jobSalary':'4k-5k','jobDescription':'Help to fix technical issues'},{'companyPicture':SimpleUploadedFile(name="Company Picture",content=f.read())})
            self.assertTrue(form.is_valid())

    def test_jobTitle_label(self):
        form=jobsCreate()
        self.assertTrue(form.fields['jobTitle'].label is None or form.fields['jobTitle'].label == 'Job Title')

    def test_companyName_label(self):
        form=jobsCreate()
        self.assertTrue(form.fields['companyName'].label is None or form.fields['companyName'].label == 'Company Name')

    def test_jobSalary_label(self):
        form=jobsCreate()
        self.assertTrue(form.fields['jobSalary'].label is None or form.fields['jobSalary'].label == 'Job Salary')

    def test_jobDescription_label(self):
        form=jobsCreate()
        self.assertTrue(form.fields['jobDescription'].label is None or form.fields['jobDescription'].label == 'Job Description')

class courseCreateTest(TestCase):
    def test_correct_data_type(self):
        form=courseCreate({"courseTitle":"Learn Programming","companyName":"Micron","courseDescription":"Learn Basic Programming Languages"})
        self.assertTrue(form.is_valid())

    def test_courseTitle_label(self):
        form=courseCreate()
        self.assertTrue(form.fields['courseTitle'].label is None or form.fields['courseTitle'].label == 'Course Title')

    def test_companyName_label(self):
        form=courseCreate()
        self.assertTrue(form.fields['companyName'].label is None or form.fields['companyName'].label == 'Company Name')

    def test_courseDescription_label(self):
        form=courseCreate()
        self.assertTrue(form.fields['courseDescription'].label is None or form.fields['courseDescription'].label == 'Course Description')
    
class articleCreateTest(TestCase):
    def test_correct_data_type(self):
        form=articleCreate({"articleTitle":"How to write resume","articleDescription":"Learn how to write convincing resumes"})
        self.assertTrue(form.is_valid())

    def test_courseTitle_label(self):
        form=articleCreate()
        self.assertTrue(form.fields['articleTitle'].label is None or form.fields['articleTitle'].label == 'Article Title')

    def test_articleDescription_label(self):
        form=articleCreate()
        self.assertTrue(form.fields['articleDescription'].label is None or form.fields['articleDescription'].label == 'Article Description')
    
class contributorProfilePageFormTest(TestCase):
    def test_correct_data_type(self):
        form=ContributorProfilePageForm({"username":"bt123","password":"abc123!@#"})
        self.assertTrue(form.is_valid())