from django.db import models

# Create your models here.
from django.db import models

class student(models.Model):
    studentid=models.AutoField
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    date=models.DateField(null=True)
    studentimage=models.ImageField(upload_to='image',default="")

    def __str__(self):
        return self.username
