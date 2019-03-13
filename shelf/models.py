from django.db import models
from django.urls import reverse


class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Category(models.Model):
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse("books-by-category", args=[str(self.id)])
    

class Book(models.Model):
    title = models.CharField(max_length=255)
    authors = models.ManyToManyField("Author", related_name='books')
    description = models.TextField(max_length=1000)
    url = models.TextField(max_length=1000)
    date_added = models.DateField(auto_now_add=True)
    categories = models.ManyToManyField(Category, related_name='books')

    def __str__(self):
        return self.title

    class Meta:
        ordering=['-date_added']
    