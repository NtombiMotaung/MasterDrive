from django.db import models


class HeadPicture(models.Model):
    image = models.ImageField(
        upload_to="posts/bg/",
    )