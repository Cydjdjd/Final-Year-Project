from django.test import TestCase

from contributor.models import Job,Course,Article,JobApplicationDetails,CourseApplicationDetails
from general.models import User,NormalUser,Contributor
class JobModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create(username="mt123",password="abc123!@#",is_contributor=True)
        Contributor.objects.create(user_id=1)
        Job.objects.create(companyPicture="contributor\tests\images\google.jpg",jobTitle="Web developer",companyName="Google",jobSalary="4k-5k",jobDescription="Developing Web Applications in C#",contributor_id=1)

    def test_companyPicture_label(self):
        job=Job.objects.get(id=1)
        field_label = job._meta.get_field('companyPicture').verbose_name
        self.assertEqual(field_label, 'companyPicture')

    def test_companyPicture_correct_url(self):
        job=Job.objects.get(id=1)
        companyPicture=job.companyPicture
        self.assertEqual(companyPicture,'contributor\tests\images\google.jpg')

    def test_companyPicture_incorrect_url(self):
        job=Job.objects.get(id=1)
        companyPicture=job.companyPicture
        self.assertNotEqual(companyPicture,'google.jpg')

    def test_jobTitle_label(self):
        job=Job.objects.get(id=1)
        field_label = job._meta.get_field('jobTitle').verbose_name
        self.assertEqual(field_label, 'jobTitle')

    def test_jobTitle_type(self):
        job=Job.objects.get(id=1)
        type = job._meta.get_field('jobTitle').get_internal_type()
        self.assertEqual(type, 'CharField')

    def test_companyName_label(self):
        job=Job.objects.get(id=1)
        field_label = job._meta.get_field('companyName').verbose_name
        self.assertEqual(field_label, 'companyName')

    def test_companyName_type(self):
        job=Job.objects.get(id=1)
        type = job._meta.get_field('companyName').get_internal_type()
        self.assertEqual(type, 'CharField')

    def test_jobSalary_label(self):
        job=Job.objects.get(id=1)
        field_label = job._meta.get_field('jobSalary').verbose_name
        self.assertEqual(field_label, 'jobSalary')

    def test_jobSalary_type(self):
        job=Job.objects.get(id=1)
        type = job._meta.get_field('jobSalary').get_internal_type()
        self.assertEqual(type, 'CharField')

    def test_jobDescription_label(self):
        job=Job.objects.get(id=1)
        field_label = job._meta.get_field('jobDescription').verbose_name
        self.assertEqual(field_label, 'jobDescription')

    def test_jobDescription_type(self):
        job=Job.objects.get(id=1)
        type = job._meta.get_field('jobDescription').get_internal_type()
        self.assertEqual(type, 'CharField')

    def test_contributor_label(self):
        job=Job.objects.get(id=1)
        field_label = job._meta.get_field('contributor').verbose_name
        self.assertEqual(field_label, 'contributor')

    def test_contributor_correct_id(self):
        job=Job.objects.get(id=1)
        id=job.contributor_id
        self.assertEqual(id,1)

    def test_contributor_incorrect_id(self):
        job=Job.objects.get(id=1)
        id=job.contributor_id
        self.assertNotEqual(id,2)

class CourseModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create(username="mt123",password="abc123!@#",is_contributor=True)
        Contributor.objects.create(user_id=1)
        Course.objects.create(courseTitle="Game Development",companyName="IBM",courseDescription="Learn about game development",contributor_id = 1)

    def test_courseTitle_label(self):
        course=Course.objects.get(id=1)
        field_label = course._meta.get_field('courseTitle').verbose_name
        self.assertEqual(field_label, 'courseTitle')

    def test_courseTitle_type(self):
        course=Course.objects.get(id=1)
        type = course._meta.get_field('courseTitle').get_internal_type()
        self.assertEqual(type, 'CharField')

    def test_companyName_label(self):
        course=Course.objects.get(id=1)
        field_label = course._meta.get_field('companyName').verbose_name
        self.assertEqual(field_label, 'companyName')

    def test_companyName_type(self):
        course=Course.objects.get(id=1)
        type = course._meta.get_field('companyName').get_internal_type()
        self.assertEqual(type, 'CharField')

    def test_courseDescription_label(self):
        course=Course.objects.get(id=1)
        field_label = course._meta.get_field('courseDescription').verbose_name
        self.assertEqual(field_label, 'courseDescription')

    def test_courseDescription_type(self):
        course=Course.objects.get(id=1)
        type = course._meta.get_field('courseDescription').get_internal_type()
        self.assertEqual(type, 'CharField')
    def test_contributor_label(self):
        course=Course.objects.get(id=1)
        field_label = course._meta.get_field('contributor').verbose_name
        self.assertEqual(field_label, 'contributor')

    def test_contributor_correct_id(self):
        course=Course.objects.get(id=1)
        id=course.contributor_id
        self.assertEqual(id,1)

    def test_contributor_incorrect_id(self):
        course=Course.objects.get(id=1)
        id=course.contributor_id
        self.assertNotEqual(id,2)
 
class ArticleModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create(username="mt123",password="abc123!@#",is_contributor=True)
        Contributor.objects.create(user_id=1)
        Article.objects.create(articleTitle="Resume making",articleDescription="Learn about resume making",contributor_id = 1)

    def test_articleTitle_label(self):
        article=Article.objects.get(id=1)
        field_label = article._meta.get_field('articleTitle').verbose_name
        self.assertEqual(field_label, 'articleTitle')

    def test_articleTitle_type(self):
        article=Article.objects.get(id=1)
        type = article._meta.get_field('articleTitle').get_internal_type()
        self.assertEqual(type, 'CharField')

    def test_articleDescription_label(self):
        article=Article.objects.get(id=1)
        field_label = article._meta.get_field('articleDescription').verbose_name
        self.assertEqual(field_label, 'articleDescription')

    def test_articleDescription_type(self):
        article=Article.objects.get(id=1)
        type = article._meta.get_field('articleDescription').get_internal_type()
        self.assertEqual(type, 'CharField')
    
    def test_contributor_label(self):
        article=Article.objects.get(id=1)
        field_label = article._meta.get_field('contributor').verbose_name
        self.assertEqual(field_label, 'contributor')

    def test_contributor_correct_id(self):
        article=Article.objects.get(id=1)
        id=article.contributor_id
        self.assertEqual(id,1)

    def test_contributor_incorrect_id(self):
        article=Article.objects.get(id=1)
        id=article.contributor_id
        self.assertNotEqual(id,2)

class JobApplicationDetailsModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create(username="mt123",password="abc123!@#",is_normal=True)
        NormalUser.objects.create(user_id=1)
        User.objects.create(username="at123",password="abc123!@#",is_contributor=True)
        Contributor.objects.create(user_id=2)
        Job.objects.create(companyPicture="contributor\tests\images\google.jpg",jobTitle="Web developer",companyName="Google",jobSalary="4k-5k",jobDescription="Developing Web Applications in C#",contributor_id=1)
        JobApplicationDetails.objects.create(userApplied_id=1,jobApplied_id=1,jobTitle="Full Stack Developer",companyName="Microsoft",userName="mt123",realName="Mary Tan",age=54,resume="contributor\tests\resumes\functionalSample.pdf")

    def test_userApplied_label(self):
        jobApplication=JobApplicationDetails.objects.get(id=1)
        field_label = jobApplication._meta.get_field('userApplied').verbose_name
        self.assertEqual(field_label, 'userApplied')

    def test_userApplied_correct_id(self):
        jobApplication=JobApplicationDetails.objects.get(id=1)
        id=jobApplication.userApplied_id
        self.assertEqual(id,1)

    def test_userApplied_incorrect_id(self):
        jobApplication=JobApplicationDetails.objects.get(id=1)
        id=jobApplication.userApplied_id
        self.assertNotEqual(id,2)

    def test_jobApplied_label(self):
        jobApplication=JobApplicationDetails.objects.get(id=1)
        field_label = jobApplication._meta.get_field('jobApplied').verbose_name
        self.assertEqual(field_label, 'jobApplied')

    def test_jobApplied_correct_id(self):
        jobApplication=JobApplicationDetails.objects.get(id=1)
        id=jobApplication.jobApplied_id
        self.assertEqual(id,1)

    def test_jobApplied_incorrect_id(self):
        jobApplication=JobApplicationDetails.objects.get(id=1)
        id=jobApplication.jobApplied_id
        self.assertNotEqual(id,2)

    def test_jobTitle_label(self):
        jobApplication=JobApplicationDetails.objects.get(id=1)
        field_label = jobApplication._meta.get_field('jobTitle').verbose_name
        self.assertEqual(field_label, 'jobTitle')

    def test_jobTitle_type(self):
        jobApplication=JobApplicationDetails.objects.get(id=1)
        type = jobApplication._meta.get_field('jobTitle').get_internal_type()
        self.assertEqual(type, 'CharField')

    def test_companyName_label(self):
        jobApplication=JobApplicationDetails.objects.get(id=1)
        field_label = jobApplication._meta.get_field('companyName').verbose_name
        self.assertEqual(field_label, 'companyName')

    def test_companyName_type(self):
        jobApplication=JobApplicationDetails.objects.get(id=1)
        type = jobApplication._meta.get_field('companyName').get_internal_type()
        self.assertEqual(type, 'CharField')
    
    def test_userName_label(self):
        jobApplication=JobApplicationDetails.objects.get(id=1)
        field_label = jobApplication._meta.get_field('userName').verbose_name
        self.assertEqual(field_label, 'userName')

    def test_userName_type(self):
        jobApplication=JobApplicationDetails.objects.get(id=1)
        type = jobApplication._meta.get_field('userName').get_internal_type()
        self.assertEqual(type, 'CharField')

    def test_realName_label(self):
        jobApplication=JobApplicationDetails.objects.get(id=1)
        field_label = jobApplication._meta.get_field('realName').verbose_name
        self.assertEqual(field_label, 'realName')

    def test_realName_type(self):
        jobApplication=JobApplicationDetails.objects.get(id=1)
        type = jobApplication._meta.get_field('realName').get_internal_type()
        self.assertEqual(type, 'CharField')

    def test_age_label(self):
        jobApplication=JobApplicationDetails.objects.get(id=1)
        field_label = jobApplication._meta.get_field('age').verbose_name
        self.assertEqual(field_label, 'age')

    def test_age_type(self):
        jobApplication=JobApplicationDetails.objects.get(id=1)
        type = jobApplication._meta.get_field('age').get_internal_type()
        self.assertEqual(type, 'IntegerField')

    def test_resume_label(self):
        jobApplication=JobApplicationDetails.objects.get(id=1)
        field_label = jobApplication._meta.get_field('resume').verbose_name
        self.assertEqual(field_label, 'resume')

    def test_resume_correct_url(self):
        jobApplication=JobApplicationDetails.objects.get(id=1)
        resume=jobApplication.resume
        self.assertEqual(resume,'contributor\tests\resumes\functionalSample.pdf')

    def test_resume_incorrect_url(self):
        jobApplication=JobApplicationDetails.objects.get(id=1)
        resume=jobApplication.resume
        self.assertNotEqual(resume,'functionalSample.pdf')

    
class CourseApplicationDetailsModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create(username="mt123",password="abc123!@#",is_normal=True)
        NormalUser.objects.create(user_id=1)
        User.objects.create(username="at123",password="abc123!@#",is_contributor=True)
        Contributor.objects.create(user_id=2)
        Course.objects.create(courseTitle="Game Development",companyName="IBM",courseDescription="Learn about game development",contributor_id = 1)
        CourseApplicationDetails.objects.create(userApplied_id=1,courseApplied_id=1,courseTitle="Game Development",companyName="IBM",userName="mt123",realName="Mary Tan",age=54,startDate="23 October 2024")

    def test_userApplied_label(self):
        courseApplication=CourseApplicationDetails.objects.get(id=1)
        field_label = courseApplication._meta.get_field('userApplied').verbose_name
        self.assertEqual(field_label, 'userApplied')

    def test_userApplied_correct_id(self):
        courseApplication=CourseApplicationDetails.objects.get(id=1)
        id=courseApplication.userApplied_id
        self.assertEqual(id,1)

    def test_userApplied_incorrect_id(self):
        courseApplication=CourseApplicationDetails.objects.get(id=1)
        id=courseApplication.userApplied_id
        self.assertNotEqual(id,2)

    def test_courseApplied_label(self):
        courseApplication=CourseApplicationDetails.objects.get(id=1)
        field_label = courseApplication._meta.get_field('courseApplied').verbose_name
        self.assertEqual(field_label, 'courseApplied')

    def test_courseApplied_correct_id(self):
        courseApplication=CourseApplicationDetails.objects.get(id=1)
        id=courseApplication.courseApplied_id
        self.assertEqual(id,1)

    def test_courseApplied_incorrect_id(self):
        courseApplication=CourseApplicationDetails.objects.get(id=1)
        id=courseApplication.courseApplied_id
        self.assertNotEqual(id,2)

    def test_courseTitle_label(self):
        courseApplication=CourseApplicationDetails.objects.get(id=1)
        field_label = courseApplication._meta.get_field('courseTitle').verbose_name
        self.assertEqual(field_label, 'courseTitle')

    def test_courseTitle_type(self):
        courseApplication=CourseApplicationDetails.objects.get(id=1)
        type = courseApplication._meta.get_field('courseTitle').get_internal_type()
        self.assertEqual(type, 'CharField')

    def test_companyName_label(self):
        courseApplication=CourseApplicationDetails.objects.get(id=1)
        field_label = courseApplication._meta.get_field('companyName').verbose_name
        self.assertEqual(field_label, 'companyName')

    def test_companyName_type(self):
        courseApplication=CourseApplicationDetails.objects.get(id=1)
        type = courseApplication._meta.get_field('companyName').get_internal_type()
        self.assertEqual(type, 'CharField')
    
    def test_userName_label(self): 
        courseApplication=CourseApplicationDetails.objects.get(id=1)
        field_label = courseApplication._meta.get_field('userName').verbose_name
        self.assertEqual(field_label, 'userName')

    def test_userName_type(self):
        courseApplication=CourseApplicationDetails.objects.get(id=1)
        type = courseApplication._meta.get_field('userName').get_internal_type()
        self.assertEqual(type, 'CharField')

    def test_realName_label(self):
        courseApplication=CourseApplicationDetails.objects.get(id=1)
        field_label = courseApplication._meta.get_field('realName').verbose_name
        self.assertEqual(field_label, 'realName')

    def test_realName_type(self):
        courseApplication=CourseApplicationDetails.objects.get(id=1)
        type = courseApplication._meta.get_field('realName').get_internal_type()
        self.assertEqual(type, 'CharField')

    def test_age_label(self):
        courseApplication=CourseApplicationDetails.objects.get(id=1)
        field_label = courseApplication._meta.get_field('age').verbose_name
        self.assertEqual(field_label, 'age')

    def test_age_type(self):
        courseApplication=CourseApplicationDetails.objects.get(id=1)
        type = courseApplication._meta.get_field('age').get_internal_type()
        self.assertEqual(type, 'IntegerField')

    def test_startDate_label(self):
        courseApplication=CourseApplicationDetails.objects.get(id=1)
        field_label = courseApplication._meta.get_field('startDate').verbose_name
        self.assertEqual(field_label, 'startDate')

    def test_startDate_type(self):
        courseApplication=CourseApplicationDetails.objects.get(id=1)
        type = courseApplication._meta.get_field('startDate').get_internal_type()
        self.assertEqual(type, 'CharField')