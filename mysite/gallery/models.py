from django.db import models

class HomePicture(models.Model):
    image = models.ImageField(
        upload_to="posts/bg/",
    )

class WelcomePicture(models.Model):
    image = models.ImageField(
        upload_to="posts/bg/",
    )

class GalleryBackground(models.Model):
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
    image4 = models.ImageField(
    upload_to="posts/bg/",
    )
    image5 = models.ImageField(
    upload_to="posts/bg/",
    )
    image6 = models.ImageField(
    upload_to="posts/bg/",
    )
    image7 = models.ImageField(
    upload_to="posts/bg/",
    )
    image8 = models.ImageField(
    upload_to="posts/bg/",
    )
    image9 = models.ImageField(
    upload_to="posts/bg/",
    )


