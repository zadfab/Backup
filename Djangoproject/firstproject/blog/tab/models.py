from django.db import models


# Create your models here.
class tab(models.Model):
    Dataid = models.AutoField
    stdname = models.CharField(max_length=50)
    rollno = models.IntegerField(max_length=50)
    stdfee = models.IntegerField(max_length=50)
    stdnImage = models.ImageField(upload_to='images', default="")

    def __str__(self):
        return self.stdname
