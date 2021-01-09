from django.db import models

# Create your models here.
class scheduler_table(models.Model):
    id = models.AutoField
    scheduler_id = models.CharField(max_length=100)
    time_stamp = models.CharField(max_length=30,)
    status = models.BooleanField()

    def __str__(self):
        return self.time_stamp

class message_forwarding_log(models.Model):
    scheduler_id = models.IntegerField(default=0)
    message_id = models.IntegerField()
    email_address = models.CharField(max_length=30)
    status = models.BooleanField()
    remark = models.CharField(max_length=30)

    def __str__(self):
        return self.email_address

class customer_table(models.Model):
    id = models.AutoField
    customer_name = models.CharField(max_length=30,default="")
    ezzy_id = models.CharField(max_length=100)

    email_address = models.CharField(max_length=30)
    phone_number = models.IntegerField()
    DND_status = models.BooleanField(default=False)
    opt_out_template_status = models.BooleanField(default=False)

    def __str__(self):
        return self.customer_name

class template_table(models.Model):
    template_id = models.IntegerField(default=0)
    template_name = models.CharField(max_length=30)
    template_name_on_cm_com = models.CharField(max_length=30)

    def __str__(self):
        return self.template_name




