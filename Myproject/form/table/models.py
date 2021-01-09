from django.db import models


# Create your models here.

class form(models.Model):
    name=models.CharField(max_length=20)
    rollnumber=models.IntegerField(max_length=20,primary_key=True)
    address=models.CharField(max_length=20)

    def __str__(self):
        return self.name

class forminfo(models.Model):
    eid=models.IntegerField()

    