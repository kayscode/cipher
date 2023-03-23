from django.db import models


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    password = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    avatar = models.ImageField(upload_to='images', null=True, blank=True)


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    receiver = models.IntegerField()
    text = models.TextField()
    sent = models.DateField(auto_now=True)
    cipher_key = models.CharField(max_length=10)
