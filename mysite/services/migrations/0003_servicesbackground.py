# Generated by Django 4.0.4 on 2022-06-01 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_contactimages'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServicesBackground',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='posts/bg/')),
            ],
        ),
    ]
