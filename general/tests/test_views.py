from django.test import TestCase
from django.urls import reverse
from general.models import User,Contributor,NormalUser
from django.core.files.uploadedfile import SimpleUploadedFile
from urllib.parse import urlencode

class GeneralViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(username="jt123",password="abc123!@#",is_normal=True)
        User.objects.create_user(username="MrBoss",password="abc123!@#",is_contributor=True)
    
    def test_homepage(self):
        response = self.client.get(reverse('originalhome'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'generalhome.html')

    def test_normalUser_login_success(self):
        data=urlencode({"username":"jt123","password":"abc123!@#"})
        response = self.client.post(reverse('loginpageuser'),data,content_type="application/x-www-form-urlencoded")
        self.assertEqual(response.status_code, 302)
    
    def test_normalUser_login_failure(self):
        data=urlencode({"username":"wrongusername","password":"wrongpassword"})
        response = self.client.post(reverse('loginpageuser'),data,content_type="application/x-www-form-urlencoded")
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'loginpageuser.html')

    def test_contributor_login_success(self):
        data=urlencode({"username":"MrBoss","password":"abc123!@#"})
        response = self.client.post(reverse('loginpagecontributor'),data,content_type="application/x-www-form-urlencoded")
        self.assertEqual(response.status_code, 302)
    
    def test_contributor_login_failure(self):
        data=urlencode({"username":"wrongusername","password":"wrongpassword"})
        response = self.client.post(reverse('loginpagecontributor'),data,content_type="application/x-www-form-urlencoded")
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'loginpagecontributor.html')

    def test_normalUser_signup(self):
        with open('general/tests/images/icImage.jpg', 'rb') as f:
            data={"username":"mary123","password1":"abc123!@#","password2":"abc123!@#","age":56,"ic":SimpleUploadedFile(name="IC",content=f.read(),content_type='image/jpg')}
            response = self.client.post(reverse('signuppageuser'),data)
            self.assertEqual(response.status_code, 302)

    def test_contributor_signup(self):
        data=urlencode({"username":"NewContributor","password1":"abc123!@#","password2":"abc123!@#"})
        response = self.client.post(reverse('signuppagecontributor'),data,content_type="application/x-www-form-urlencoded")
        self.assertEqual(response.status_code, 302)

    def test_aboutPage(self):
        response = self.client.get(reverse('originalaboutPage'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'aboutPage.html')

    def test_getcontributorsignuppage(self):
        response = self.client.get(reverse('signuppagecontributor'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signuppagecontributor.html')

    def test_getusersignuppage(self):
        response = self.client.get(reverse('signuppageuser'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signuppageuser.html')

    def test_getcontributorloginpage(self):
        response = self.client.get(reverse('loginpagecontributor'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'loginpagecontributor.html')

    def test_getuserloginpage(self):
        response = self.client.get(reverse('loginpageuser'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'loginpageuser.html')

