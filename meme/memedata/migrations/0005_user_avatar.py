# Generated by Django 3.1.2 on 2021-01-25 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memedata', '0004_teststar'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatars'),
        ),
    ]
