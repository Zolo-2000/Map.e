from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User)
    charter = models.CharField(max_length=13, blank=True)
    birthday = models.DateField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
