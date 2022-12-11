from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

UserModel = get_user_model()


class ChatRoom(models.Model):
    MAX_LEN_NAME = 64
    name = models.CharField(max_length=MAX_LEN_NAME, unique=True)
    users = models.ManyToManyField(UserModel)


class Message(models.Model):
    sender = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    chat_room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
