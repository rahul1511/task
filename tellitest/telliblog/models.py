from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Creating a model which is subclass of models ,with some field

class BlogPost(models.Model):
    author      = models.ForeignKey(User, on_delete=models.CASCADE)
    title       = models.CharField(max_length=100)
    content     = models.TextField(max_length=200)
    posted_date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.title




