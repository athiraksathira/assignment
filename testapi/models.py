from django.db import models


# Create your models here.
class UserModel(models.Model):
    name = models.CharField(max_length=120, unique=True)
    date=models.DateTimeField()

    email = models.EmailField()
    income = models.PositiveIntegerField()
    ipaddress = models.GenericIPAddressField()


def __str__(self):
    return self.name
