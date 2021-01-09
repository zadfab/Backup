from django.db import models

# Create your models here.
class blogdb(models.Model):
    title=models.CharField(max_length=10)
    appname=models.CharField(max_length=10)
    size=models.CharField(max_length=10)


    def __str__(self):
        return self.title