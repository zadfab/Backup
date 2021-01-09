from django.db import models

# Create your models here.

class student(models.Model):
    name = models.CharField(max_length=20,default="")
    rollno = models.IntegerField(unique= True)
    school_name = models.CharField(max_length=20,default="")
    phoneno = models.CharField(max_length=20,default="")
    email = models.CharField(max_length=20,default="")

    def __str__(self):
        return self.name

