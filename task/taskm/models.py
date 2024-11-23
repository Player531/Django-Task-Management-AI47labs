from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default = False)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class OAuthKeys(models.Model):
    name = models.CharField(max_length=100)
    client_id = models.CharField(max_length=255)
    client_secret = models.CharField(max_length=255)

class SendInvitation(models.Model):
    email = models.EmailField()