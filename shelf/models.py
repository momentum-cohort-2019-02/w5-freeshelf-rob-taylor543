from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Category(models.Model):
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse("category-list", args=[str(self.id)])
    

class Book(models.Model):
    title = models.CharField(max_length=255)
    authors = models.ManyToManyField("Author", related_name='books')
    description = models.TextField(max_length=1000)
    url = models.TextField(max_length=1000)
    date_added = models.DateField(auto_now_add=True)
    categories = models.ManyToManyField(Category, related_name='books')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering=['-date_added']

    def save(self, *args, **kwargs):
        self.set_slug()
        super().save(*args, **kwargs)

    def set_slug(self):
        if self.slug:
            return

        base_slug = slugify(self.title)
        slug = base_slug
        n=0

        while Book.objects.filter(slug=slug).count():
            n+=1
            slug = base_slug + "-" + str(n)

        self.slug=slug
    