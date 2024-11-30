from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=150)


class Book(models.Model):
    title = models.CharField(max_length=150)
    publication_year = models.DateField()
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name="author_books")
