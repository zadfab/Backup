from django.db import models

# Create your models here.

class countrymaster(models.Model):
    cid=models.IntegerField(default=True)
    countryname=models.CharField(max_length=20)


    def __str__(self):
        return self.countryname


class statemaster(models.Model):
    sid=models.AutoField
    cid=models.IntegerField()
    statename=models.CharField(max_length=20)


    def __str__(self):
        return self.statename