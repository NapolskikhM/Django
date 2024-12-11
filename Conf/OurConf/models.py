from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    """пост в конференции с привязкой к автору"""
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
