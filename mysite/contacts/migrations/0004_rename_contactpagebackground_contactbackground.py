# Generated by Django 4.0.4 on 2022-06-01 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_contactpagebackground'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ContactPageBackground',
            new_name='ContactBackground',
        ),
    ]
