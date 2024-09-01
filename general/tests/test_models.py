from django.test import TestCase
from general.models import User,NormalUser,Contributor

class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create(username="mt123",password="abc123!@#",is_contributor=True)
        User.objects.create(username="jt123",password="abc123!@#",is_normal=True)
        User.objects.create(username="lt123",password="abc123!@#",is_contributor=True)

    def test_username_label(self):
        user=User.objects.get(id=1)
        field_label = user._meta.get_field('username').verbose_name
        self.assertEqual(field_label, 'username')

    def test_username_type(self):
        user=User.objects.get(id=1)
        type = user._meta.get_field('username').get_internal_type()
        self.assertEqual(type, 'CharField')

    def test_password_label(self):
        user=User.objects.get(id=1)
        field_label = user._meta.get_field('password').verbose_name
        self.assertEqual(field_label, 'password')

    def test_password_type(self):
        user=User.objects.get(id=1)
        type = user._meta.get_field('password').get_internal_type()
        self.assertEqual(type, 'CharField')

    def test_is_contributor_label(self):
        user=User.objects.get(id=1)
        field_label = user._meta.get_field('is_contributor').verbose_name
        self.assertEqual(field_label, 'is contributor')

    def test_is_contributor_type(self):
        job=User.objects.get(id=1)
        type = job._meta.get_field('is_contributor').get_internal_type()
        self.assertEqual(type, 'BooleanField')
    def test_is_normal_label(self):
        user=User.objects.get(id=2)
        field_label = user._meta.get_field('is_normal').verbose_name
        self.assertEqual(field_label, 'is normal')

    def test_is_normal_type(self):
        job=User.objects.get(id=2)
        type = job._meta.get_field('is_normal').get_internal_type()
        self.assertEqual(type, 'BooleanField')

class NormalUserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create(username="mt123",password="abc123!@#",is_normal=True)
        User.objects.create(username="jt123",password="abc123!@#",is_normal=True)
        User.objects.create(username="lt123",password="abc123!@#",is_normal=True)
        NormalUser.objects.create(user_id=1)
        NormalUser.objects.create(user_id=2)
        NormalUser.objects.create(user_id=3)
    
    def test_user_id_label(self):
        normalUser=NormalUser.objects.get(id=1)
        field_label = normalUser._meta.get_field('user_id').verbose_name
        self.assertEqual(field_label, 'user')

    def test_user_id_type(self):
        normalUser=NormalUser.objects.get(id=1)
        type = normalUser._meta.get_field('user_id').get_internal_type()
        self.assertEqual(type, 'OneToOneField')
class ContributorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create(username="mt123",password="abc123!@#",is_contributor=True)
        User.objects.create(username="jt123",password="abc123!@#",is_contributor=True)
        User.objects.create(username="lt123",password="abc123!@#",is_contributor=True)
        Contributor.objects.create(user_id=1)
        Contributor.objects.create(user_id=2)
        Contributor.objects.create(user_id=3)

    def test_user_id_label(self):
        contributor=Contributor.objects.get(id=1)
        field_label = contributor._meta.get_field('user_id').verbose_name
        self.assertEqual(field_label, 'user')

    def test_user_id_type(self):
        contributor=Contributor.objects.get(id=1)
        type = contributor._meta.get_field('user_id').get_internal_type()
        self.assertEqual(type, 'OneToOneField')