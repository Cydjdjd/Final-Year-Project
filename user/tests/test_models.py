from django.test import TestCase
from general.models import User,NormalUser
from user.models import careerCoachingApplicationDetails
class careerCoachingApplicationDetailsModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create(username="jt123",password="abc123!@#",is_normal=True)
        NormalUser.objects.create(user_id=1)
        careerCoachingApplicationDetails.objects.create(realName="John Tan",emailAddress="jt123@gmail.com",contactNumber="87654321",normalUserApplied_id=1)
    
    def test_realName_label(self):
        careerCoachingApplication=careerCoachingApplicationDetails.objects.get(id=1)
        field_label = careerCoachingApplication._meta.get_field('realName').verbose_name
        self.assertEqual(field_label, 'realName')

    def test_realName_type(self):
        careerCoachingApplication=careerCoachingApplicationDetails.objects.get(id=1)
        type = careerCoachingApplication._meta.get_field('realName').get_internal_type()
        self.assertEqual(type, 'CharField')

    def test_emailAddress_label(self):
        careerCoachingApplication=careerCoachingApplicationDetails.objects.get(id=1)
        field_label = careerCoachingApplication._meta.get_field('emailAddress').verbose_name
        self.assertEqual(field_label, 'emailAddress')

    def test_emailAddress_type(self):
        careerCoachingApplication=careerCoachingApplicationDetails.objects.get(id=1)
        type = careerCoachingApplication._meta.get_field('emailAddress').get_internal_type()
        self.assertEqual(type, 'CharField')

    def test_contactNumber_label(self):
        careerCoachingApplication=careerCoachingApplicationDetails.objects.get(id=1)
        field_label = careerCoachingApplication._meta.get_field('contactNumber').verbose_name
        self.assertEqual(field_label, 'contactNumber')

    def test_contactNumber_type(self):
        careerCoachingApplication=careerCoachingApplicationDetails.objects.get(id=1)
        type = careerCoachingApplication._meta.get_field('contactNumber').get_internal_type()
        self.assertEqual(type, 'CharField')

    def test_normalUserApplied_label(self):
        careerCoachingApplication=careerCoachingApplicationDetails.objects.get(id=1)
        field_label = careerCoachingApplication._meta.get_field('normalUserApplied').verbose_name
        self.assertEqual(field_label, 'normalUserApplied')

    def test_contactNumber_type(self):
        careerCoachingApplication=careerCoachingApplicationDetails.objects.get(id=1)
        type = careerCoachingApplication._meta.get_field('normalUserApplied').get_internal_type()
        self.assertEqual(type, 'ForeignKey')
