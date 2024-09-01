from user.forms import jobApplyForm,courseApplyForm,careerCoachingForm,NormalUserProfilePageForm
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

class jobApplyFormTest(TestCase):
    def test_correct_data_type(self):
        with open('user/tests/resumes/functionalSample.pdf', 'rb') as f:
            form=jobApplyForm({'jobTitle':'Web Developer','companyName':'Google','userName':'BobTan123','realName':'Bob Tan','age':56},{'resume':SimpleUploadedFile(name="resume",content=f.read())})
            self.assertTrue(form.is_valid())

    def test_jobTitle_label(self):
        form=jobApplyForm()
        self.assertTrue(form.fields['jobTitle'].label is None or form.fields['jobTitle'].label == 'Job Title')

    def test_companyName_label(self):
        form=jobApplyForm()
        self.assertTrue(form.fields['companyName'].label is None or form.fields['companyName'].label == 'Company')

    def test_userName_label(self):
        form=jobApplyForm()
        self.assertTrue(form.fields['userName'].label is None or form.fields['userName'].label == 'Username')

    def test_realName_label(self):
        form=jobApplyForm()
        self.assertTrue(form.fields['realName'].label is None or form.fields['realName'].label == 'Real Name')

    def test_age_label(self):
        form=jobApplyForm()
        self.assertTrue(form.fields['age'].label is None or form.fields['age'].label == 'Age')

    def test_resume_label(self):
        form=jobApplyForm()
        self.assertTrue(form.fields['resume'].label is None or form.fields['resume'].label == 'Resume')

class courseApplyFormTest(TestCase):
    def test_correct_data_type(self):
        form=courseApplyForm({'courseTitle':'Web Development','companyName':'Google','userName':'BobTan123','realName':'Bob Tan','age':56,'startDate':'24 September 2024'})
        self.assertTrue(form.is_valid())

    def test_courseTitle_label(self):
        form=courseApplyForm()
        self.assertTrue(form.fields['courseTitle'].label is None or form.fields['courseTitle'].label == 'Course Title')

    def test_companyName_label(self):
        form=courseApplyForm()
        self.assertTrue(form.fields['companyName'].label is None or form.fields['companyName'].label == 'Company')

    def test_userName_label(self):
        form=courseApplyForm()
        self.assertTrue(form.fields['userName'].label is None or form.fields['userName'].label == 'Username')

    def test_realName_label(self):
        form=courseApplyForm()
        self.assertTrue(form.fields['realName'].label is None or form.fields['realName'].label == 'Real Name')

    def test_age_label(self):
        form=courseApplyForm()
        self.assertTrue(form.fields['age'].label is None or form.fields['age'].label == 'Age')

    def test_resume_label(self):
        form=courseApplyForm()
        self.assertTrue(form.fields['startDate'].label is None or form.fields['startDate'].label == 'Start Date')


class careerCoachingFormTest(TestCase):
    def test_correct_data_type(self):
        form=careerCoachingForm({'realName':'Bob Tan','emailAddress':'bobtan123@gmail.com','contactNumber':'87654321'})
        self.assertTrue(form.is_valid())

    def test_realName_label(self):
        form=careerCoachingForm()
        self.assertTrue(form.fields['realName'].label is None or form.fields['realName'].label == 'Real Name')

    def test_age_label(self):
        form=careerCoachingForm()
        self.assertTrue(form.fields['emailAddress'].label is None or form.fields['emailAddress'].label == 'Email Address')

    def test_contactNumber_label(self):
        form=careerCoachingForm()
        self.assertTrue(form.fields['contactNumber'].label is None or form.fields['contactNumber'].label == 'Contact Number')

class NormalUserProfilePageFormTest(TestCase):
    def test_correct_data_type(self):
        with open('general/tests/images/icImage.jpg', 'rb') as f:
            form=NormalUserProfilePageForm({'username':'BobTan123','password':'abc123!@#', 'age':56},{'ic':SimpleUploadedFile(name="IC",content=f.read())})
            self.assertTrue(form.is_valid())

    def test_username_label(self):
        form=NormalUserProfilePageForm()
        self.assertTrue(form.fields['username'].label is None or form.fields['username'].label == 'Username')

    def test_password_label(self):
        form=NormalUserProfilePageForm()
        self.assertTrue(form.fields['password'].label is None or form.fields['password'].label == 'Password')

    def test_age_label(self):
        form=NormalUserProfilePageForm()
        self.assertTrue(form.fields['age'].label is None or form.fields['age'].label == 'Age')

    def test_ic_label(self):
        form=NormalUserProfilePageForm()
        self.assertTrue(form.fields['ic'].label is None or form.fields['ic'].label == 'ic')