# Generated by Django 4.0.4 on 2022-06-06 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0008_rename_backgroundimage_gallerybackground'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePicture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='posts/bg/')),
            ],
        ),
    ]
