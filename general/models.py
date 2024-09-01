from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_normal = models.BooleanField(default=False)
    is_contributor = models.BooleanField(default=False)

# Create your models here.
class NormalUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True, blank=True)
    age=models.IntegerField(null=True, blank=True)
    ic=models.FileField(upload_to ='images/')

class Contributor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True, blank=True)