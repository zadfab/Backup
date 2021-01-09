from django.db import models

# Create your models here.
class student(models.Model):
    stdid=models.AutoField
    stdname=models.CharField(max_length=10)
    #dob=models.DateField()
    rollno=models.IntegerField(max_length=20)

    def __str__(self):
        return self.stdname