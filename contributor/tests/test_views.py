from django.test import TestCase
from contributor.models import Job,Course,Article
from general.models import User,Contributor,NormalUser
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from urllib.parse import urlencode

class ContributorViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_contributors=10
        for contributor_id in range(1,number_of_contributors+1):
            User.objects.create_user(username='mt'+str(contributor_id),password="abc123!@#",is_contributor=True)
            Contributor.objects.create(user_id=contributor_id)

        number_of_jobs=10
        for job_id in range(number_of_jobs):
            Job.objects.create(companyPicture="contributor\tests\images\google.jpg",jobTitle="Web developer",companyName="Google",jobSalary="4k-5k",jobDescription="Developing Web Applications in C#",contributor_id=1)
            Course.objects.create(courseTitle="Game Development",companyName="IBM",courseDescription="Learn about game development",contributor_id = 1)
            Article.objects.create(articleTitle="Resume making",articleDescription="Learn about resume making",contributor_id = 1)

    def test_homepage(self):
        self.client.login(username='mt1', password='abc123!@#')
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contributorhomepage.html')
    def test_logout(self):
        self.client.login(username='mt1', password='abc123!@#')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)

    def test_createhistorypage(self):
        self.client.login(username='mt1', password='abc123!@#')
        response = self.client.get(reverse('createhistorypage'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contributorcreatehistory.html')

    def test_createhistorypage2(self):
        self.client.login(username='mt1', password='abc123!@#')
        response = self.client.get(reverse('createhistorypage2'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contributorcreatehistory2.html')
    def test_createhistorypage3(self):
        self.client.login(username='mt1', password='abc123!@#')
        response = self.client.get(reverse('createhistorypage3'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contributorcreatehistory3.html')
    def test_createpage(self):
        self.client.login(username='mt1', password='abc123!@#')
        response = self.client.get(reverse('createpage1'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contributorcreatepage1.html')

    def test_createpage2(self):
        self.client.login(username='mt1', password='abc123!@#')
        response = self.client.get(reverse('createpage2'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contributorcreatepage2.html')

    def test_createpage3(self):
        self.client.login(username='mt1', password='abc123!@#')
        response = self.client.get(reverse('createpage3'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contributorcreatepage3.html')

    def test_editPage1(self):
        self.client.login(username='mt1', password='abc123!@#')
        response = self.client.get(reverse('editpage1', kwargs={'job_id':4}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contributoreditpage1.html')

    def test_editPage2(self):
        self.client.login(username='mt1', password='abc123!@#')
        response = self.client.get(reverse('editpage2', kwargs={'course_id':4}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contributoreditpage2.html')

    def test_editPage3(self):
        self.client.login(username='mt1', password='abc123!@#')
        response = self.client.get(reverse('editpage3', kwargs={'article_id':4}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contributoreditpage3.html')

    def test_contributorProfilePage(self):
        self.client.login(username='mt1', password='abc123!@#')
        response = self.client.get(reverse('contributorProfilePage'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contributorProfilePage.html')

    def test_create1(self):
        self.client.login(username='mt1', password='abc123!@#')
        with open('contributor/tests/images/google.jpg', 'rb') as f:
            data = {'companyPicture':SimpleUploadedFile(name="Company Picture",content=f.read(),content_type='image/jpg'),'jobTitle':'IT Support','companyName':'Computer Support Company','jobSalary':'4k-5k','jobDescription':'Help to fix technical issues'}
            response = self.client.post(reverse('create1'),data)
            self.assertEqual(response.status_code, 302)
        

    def test_create2(self):
        self.client.login(username='mt1', password='abc123!@#')
        data =urlencode({"courseTitle":"Learn Programming","companyName":"Micron","courseDescription":"Learn Basic Programming Languages"})
        response = self.client.post(reverse('create2'),data,content_type="application/x-www-form-urlencoded")
        self.assertEqual(response.status_code, 302)

    def test_create3(self):
        self.client.login(username='mt1', password='abc123!@#')
        data=urlencode({"articleTitle":"How to write resume","articleDescription":"Learn how to write convincing resumes"})
        response = self.client.post(reverse('create3'),data,content_type="application/x-www-form-urlencoded")
        self.assertEqual(response.status_code, 302)

    def test_edit1(self):
        self.client.login(username='mt1', password='abc123!@#')
        with open('contributor/tests/images/google.jpg', 'rb') as f:
            data = {'companyPicture':SimpleUploadedFile(name="Company Picture",content=f.read(),content_type='image/jpg'),'jobTitle':'IT Support','companyName':'Computer Support Company','jobSalary':'4k-5k','jobDescription':'Help to fix technical issues'}
            response = self.client.post(reverse('edit1', kwargs={'job_id':4}),data)
            self.assertEqual(response.status_code, 302)

    def test_edit2(self):
        self.client.login(username='mt1', password='abc123!@#')
        data =urlencode({"courseTitle":"Learn Programming","companyName":"Micron","courseDescription":"Learn Basic Programming Languages"})
        response = self.client.post(reverse('edit2', kwargs={'course_id':4}),data,content_type="application/x-www-form-urlencoded")
        self.assertEqual(response.status_code, 302)

    def test_edit3(self):
        self.client.login(username='mt1', password='abc123!@#')
        data=urlencode({"articleTitle":"How to write resume","articleDescription":"Learn how to write convincing resumes"})
        response = self.client.post(reverse('edit3', kwargs={'article_id':4}),data,content_type="application/x-www-form-urlencoded")
        self.assertEqual(response.status_code, 302)

    def test_updateContributorProfilePage(self):
        self.client.login(username='mt1', password='abc123!@#')
        data=urlencode({'username':'mt123', 'password':'abc123!@#123'})
        response = self.client.post(reverse('updateContributorProfilePage'),data,content_type="application/x-www-form-urlencoded")
        self.assertEqual(response.status_code, 302)
        