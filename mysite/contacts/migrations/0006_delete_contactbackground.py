# Generated by Django 4.0.4 on 2022-07-27 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0005_delete_contactpageimage'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ContactBackground',
        ),
    ]