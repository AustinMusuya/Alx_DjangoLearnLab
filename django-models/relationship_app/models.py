from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=100)


# class Book(models.Model):
#     name = models.CharField(max_length=100)


# class Library(models.Model):
#     name = models.CharField(max_length=100)


# class Librarian(models.Model):
#     name = models.CharField(max_length=100)
