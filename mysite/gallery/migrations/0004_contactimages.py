# Generated by Django 4.0.4 on 2022-05-30 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_delete_contactimages'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', models.ImageField(upload_to='posts/bg/')),
            ],
        ),
    ]
