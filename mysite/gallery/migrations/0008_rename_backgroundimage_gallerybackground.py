# Generated by Django 4.0.4 on 2022-06-01 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0007_galleryimages_image4_galleryimages_image5_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BackgroundImage',
            new_name='GalleryBackground',
        ),
    ]