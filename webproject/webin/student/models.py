from django.db import models
from django.urls import reverse


# Create your models here.
class student(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=20)
    rollno = models.IntegerField(max_length=20)
    email = models.CharField(max_length=20)
    course = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    city = models.CharField(max_length=10)
    year = models.IntegerField(max_length=5)
    #checkbox=models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("student:studmit",kwargs={"id":self.id})
    


class studentcomment(models.Model):
    eid = models.AutoField

    comment = models.CharField(max_length=1000)




