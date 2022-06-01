from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.EmailField(max_length=150)
    message = models.TextField()

class ContactPageImage(models.Model):
    image1 = models.ImageField(
    upload_to="posts/bg/",
    )

class ContactBackground(models.Model):
    image = models.ImageField(
        upload_to = "posts/bg",
    )