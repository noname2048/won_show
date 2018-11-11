from django.db import models

# Create your models here.
class MyNum(models.Model):
    k           = models.IntegerField()
    text        = models.TextField()
    timestamp   = models.DateTimeField(auto_now_add=True)
