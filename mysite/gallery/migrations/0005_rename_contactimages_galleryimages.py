# Generated by Django 4.0.4 on 2022-05-31 04:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0004_contactimages'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ContactImages',
            new_name='GalleryImages',
        ),
    ]
