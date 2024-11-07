from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=100)


class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(Author, related_name='books')


class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, related_name='libraries')


class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, related_name='librarians')
