# Generated by Django 4.2.6 on 2025-02-24 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_alter_data_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='name',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
    ]
