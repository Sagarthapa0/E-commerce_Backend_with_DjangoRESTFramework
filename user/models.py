from django.db import models
from django.contrib.auth.models import AbstractUser

#Create your models here.


class User(AbstractUser):
    updated_at=models.DateTimeField(auto_now=True)
   

    def __str__(self) -> str:
        return self.username
