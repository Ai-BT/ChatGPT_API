from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Users(models.Model):
    USER_TYPES = (
        ('M', 'Manager'),
        ('U', 'User'),
    )
    userName = models.CharField(max_length=15, default='')
    userType = models.CharField(max_length=1, choices = USER_TYPES, default='U')
    phoneNumberRegex = RegexValidator(regex = r'^01([0|1|6|7|8|9]?)?([0-9]{3,4})?([0-9]{4})$')
    userPhone = models.CharField(validators = [phoneNumberRegex], max_length=11, unique=True, default='',primary_key=True )

    def __str__(self):
        return self.userName

    class Meta:
        verbose_name = '사용자'
        verbose_name_plural = '사용자'
