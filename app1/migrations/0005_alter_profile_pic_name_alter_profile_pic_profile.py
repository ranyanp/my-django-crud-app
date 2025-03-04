# Generated by Django 4.2.6 on 2023-11-22 07:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_alter_profile_pic_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile_pic',
            name='name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app1.data'),
        ),
        migrations.AlterField(
            model_name='profile_pic',
            name='profile',
            field=models.ImageField(default='     ', upload_to='profile'),
        ),
    ]
