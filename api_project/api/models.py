from django.db import models

# Create your models here.

# simple book model


class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
