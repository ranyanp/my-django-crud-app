# Generated by Django 4.2.6 on 2023-11-22 05:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_alter_data_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile_pic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.ImageField(upload_to='profile')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.data')),
            ],
        ),
    ]
