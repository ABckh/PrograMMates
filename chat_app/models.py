from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from bulletin_board.models import Users


class ChatModel(models.Model):
    sender = models.ForeignKey(Users, on_delete=models.CASCADE)
    message = models.TextField(null=True, blank=True)
    thread_name = models.CharField(null=True, blank=True, max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message

    class Meta:
        ordering = ['timestamp']