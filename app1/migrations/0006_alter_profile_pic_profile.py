# Generated by Django 4.2.6 on 2023-11-24 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_alter_profile_pic_name_alter_profile_pic_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile_pic',
            name='profile',
            field=models.ImageField(default='', upload_to='profile'),
        ),
    ]
