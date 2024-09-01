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
        number_of_normalusers=10
        for contributor_id in range(1,number_of_contributors+1):
            User.objects.create_user(username='mt'+str(contributor_id),password="abc123!@#",is_contributor=True)
            Contributor.objects.create(user_id=contributor_id)

        for normaluser_id in range(1+number_of_contributors,number_of_normalusers+1+number_of_contributors):
            User.objects.create_user(username='mt'+str(normaluser_id),password="abc123!@#",is_normal=True)
            NormalUser.objects.create(user_id=normaluser_id)
        number_of_jobs=10
        for job_id in range(number_of_jobs):
            Job.objects.create(companyPicture="contributor\tests\images\google.jpg",jobTitle="Web developer",companyName="Google",jobSalary="4k-5k",jobDescription="Developing Web Applications in C#",contributor_id=1)
            Course.objects.create(courseTitle="Game Development",companyName="IBM",courseDescription="Learn about game development",contributor_id = 1)
            Article.objects.create(articleTitle="Resume making",articleDescription="Learn about resume making",contributor_id = 1)

    def test_homepage(self):
        self.client.login(username='mt12', password='abc123!@#')
        response = self.client.get(reverse('normalhome'))
        self.assertEqual(response.status_code, 200)

    def test_jobPage(self):
        self.client.login(username='mt12', password='abc123!@#')
        response = self.client.get(reverse('jobPage'))
        self.assertEqual(response.status_code, 200)

    def test_coursePage(self):
        self.client.login(username='mt12', password='abc123!@#')
        response = self.client.get(reverse('coursePage'))
        self.assertEqual(response.status_code, 200)

    def test_articlesPage(self):
        self.client.login(username='mt12', password='abc123!@#')
        response = self.client.get(reverse('articlesPage'))
        self.assertEqual(response.status_code, 200)

    def test_articleReadPage(self):
        self.client.login(username='mt12', password='abc123!@#')
        response = self.client.get(reverse('articleReadPage', kwargs={'article_id':1}))
        self.assertEqual(response.status_code, 200)

    def test_jobApplyPage(self):
        self.client.login(username='mt12', password='abc123!@#')
        response = self.client.get(reverse('jobApplyPage', kwargs={'job_id':1}))
        self.assertEqual(response.status_code, 200)        

    def test_courseApplyPage(self):
        self.client.login(username='mt12', password='abc123!@#')
        response = self.client.get(reverse('courseApplyPage', kwargs={'course_id':1}))
        self.assertEqual(response.status_code, 200)        

    def test_careerCoachingPage(self):
        self.client.login(username='mt12', password='abc123!@#')
        response = self.client.get(reverse('careerCoachingPage'))
        self.assertEqual(response.status_code, 200)        

    def test_aboutPage(self):
        self.client.login(username='mt12', password='abc123!@#')
        response = self.client.get(reverse('aboutPage'))
        self.assertEqual(response.status_code, 200)        

    def test_normalUserProfilePage(self):
        self.client.login(username='mt12', password='abc123!@#')
        response = self.client.get(reverse('normalUserProfilePage'))
        self.assertEqual(response.status_code, 200)  

    def test_jobApply(self):
        self.client.login(username='mt12', password='abc123!@#')
        with open('user/tests/resumes/functionalSample.pdf', 'rb') as f:   
            data=  {'jobTitle':"Web developer",'companyName':"Google",'userName':'BobTan123','realName':'Bob Tan','age':56,'resume':SimpleUploadedFile(name="resume",content=f.read())}   
            response= self.client.post(reverse('jobApply', kwargs={'job_id':1}),data)
            self.assertEqual(response.status_code, 302)

    def test_courseApply(self):
        self.client.login(username='mt12', password='abc123!@#')
        data=  urlencode({"courseTitle":"Game Development","companyName":"IBM",'userName':'BobTan123','realName':'Bob Tan','age':56,'startDate':'24 September 2024'})
        response= self.client.post(reverse('courseApply', kwargs={'course_id':1}),data,content_type="application/x-www-form-urlencoded")
        self.assertEqual(response.status_code, 302)

    def test_submitCareerCoaching(self):
        self.client.login(username='mt12', password='abc123!@#')
        data=  urlencode({'realName':'Bob Tan','emailAddress':'bobtan123@gmail.com','contactNumber':'87654321'})
        response= self.client.post(reverse('submitCareerCoaching'),data,content_type="application/x-www-form-urlencoded")
        self.assertEqual(response.status_code, 302)

    def test_submitCareerCoaching(self):
        self.client.login(username='mt12', password='abc123!@#')
        response= self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)

    def test_updateNormalUserProfilePage(self):
        with open('general/tests/images/icImage.jpg', 'rb') as f:
            data={"username":"mary123","password":"abc123!@#","age":56,"ic":SimpleUploadedFile(name="IC",content=f.read(),content_type='image/jpg')}
            response = self.client.post(reverse('updateNormalUserProfilePage'),data)
            self.assertEqual(response.status_code, 302)