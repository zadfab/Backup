from django.db import models
from django.contrib.auth.models import  AbstractBaseUser,PermissionsMixin
from .manager import UserManager
# Create your models here.
class myuser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(unique=True,max_length=240)
    question = models.CharField(max_length=200,default="NO")
    is_customer = models.BooleanField(default=False)
    is_operator = models.BooleanField(default=False)
    is_admin    = models.BooleanField(default=False)
    is_active   = models.BooleanField(default=True)
    is_staff    = models.BooleanField(default=True)

    object = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'My User'

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''

        return self.question
