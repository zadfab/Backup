from django.db import models


# Create your models here.
class Reg(models.Model):
    regId = models.AutoField
    name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    image = models.ImageField(upload_to="student/imagess", default="")

    def __str__(self):
        return self.name;


class enquiry(models.Model):
    cadidateId = models.AutoField
    name = models.CharField(max_length=50,default=" ")
    mobilenumber = models.CharField(max_length=50,default=" ")
    email = models.CharField(max_length=50,default=" ")
    emailm = models.CharField(max_length=50,default=" ")
    domain = models.CharField(max_length=50,default=" ")
    course = models.CharField(max_length=50,default=" ")
    qualification = models.CharField(max_length=50,default=" ")
    year = models.IntegerField(default=" ")
    city = models.TextField(max_length=50,default=" ")
    date=models.DateField(null=True)


    def __str__(self):
        return self.name
