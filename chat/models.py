from django.db import models

class Message(models.Model):
    username = models.CharField(max_length=50)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username} - {self.text[:20]}"
