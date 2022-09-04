from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    @classmethod
    def create(cls, user_name, first_name, last_name, email):
        user = cls(user_name, first_name, last_name, email)
        return user


class Log(models.Model):
    description = models.ForeignKey(User, on_delete=models.CASCADE)
    calories = models.CharField(max_length=100)