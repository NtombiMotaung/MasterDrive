from django.db import models

# Create your models here.
class Service(models.Model):
    name = models.CharField(blank=False, null=False, max_length=10000)
    description = models.TextField(blank=False, null=False)
    image = models.ImageField(blank=False, null=False)

class ContactImages(models.Model):
    image1 = models.ImageField(
        upload_to="posts/bg/",
    )
    image2 = models.ImageField(
        upload_to="posts/bg/",
    )
    image3 = models.ImageField(
        upload_to="posts/bg/",
    )
    
    
