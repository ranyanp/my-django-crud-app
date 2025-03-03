from django.db import models

# Create your models here.

class data(models.Model):
    name=models.CharField(max_length=20,unique=True,null=True,default="")
    email=models.EmailField(max_length=20,unique=True,default="")
    message=models.TextField(default="")

    def __str__(self):
        return (self.name)


class Profile_pic(models.Model):
    name=models.OneToOneField(data,on_delete=models.CASCADE)
    profile=models.ImageField(upload_to='profile',default="")