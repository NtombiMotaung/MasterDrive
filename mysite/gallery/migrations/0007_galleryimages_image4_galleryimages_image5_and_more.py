# Generated by Django 4.0.4 on 2022-06-01 14:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0006_galleryimages_image2_galleryimages_image3'),
    ]

    operations = [
        migrations.AddField(
            model_name='galleryimages',
            name='image4',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='posts/bg/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='galleryimages',
            name='image5',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='posts/bg/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='galleryimages',
            name='image6',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='posts/bg/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='galleryimages',
            name='image7',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='posts/bg/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='galleryimages',
            name='image8',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='posts/bg/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='galleryimages',
            name='image9',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='posts/bg/'),
            preserve_default=False,
        ),
    ]
