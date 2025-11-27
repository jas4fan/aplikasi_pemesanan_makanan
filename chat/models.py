from django.db import models

class ChatMessage(models.Model):
    sender = models.CharField(max_length=50)
    receiver = models.CharField(max_length=50)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
