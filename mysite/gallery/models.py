from django.db import models



class BackgroundImage(models.Model):
    image = models.ImageField(
        upload_to="posts/bg/",
    )

class GalleryImages(models.Model):
    image1 = models.ImageField(
    upload_to="posts/bg/",
    )
    image2 = models.ImageField(
        upload_to="posts/bg/",
    )
    image3 = models.ImageField(
        upload_to="posts/bg/",
    )


