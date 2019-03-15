# Generated by Django 2.1.7 on 2019-03-15 18:04

from django.db import migrations
from django.conf import settings
from django.utils.text import slugify

import csv
import os.path


def load_books(apps, schema_editor):
    """Read a CSV file full of book data and insert them into the database"""
    Book = apps.get_model('shelf', 'Book')
    Author = apps.get_model('shelf', 'Author')
    Category = apps.get_model('shelf', 'Category')

    datapath = os.path.join(settings.BASE_DIR, 'initial_data')
    datafile = os.path.join(datapath, 'book_list.csv')
    Book.objects.all().delete()
    with open(datafile) as file:
        reader = csv.DictReader(file)
        for row in reader:

            if not row['authors']:
                authors, _ = Author.objects.get_or_create(name='Unknown Author')
                authors = [authors]
            else:
                authors = []
                author_list = [name for name in row['authors'].split('/')]
                for author in author_list:
                    new_author, _ = Author.objects.get_or_create(name=author)
                    authors.append(new_author)


            if not row['categories']:
                categories, _ = Category.objects.get_or_create(description='No Category')
                categories = [categories]
            else:
                categories = []
                category_list = [category for category in row['categories'].split('/')]
                for category in category_list:
                    new_category, _ = Category.objects.get_or_create(description=category)
                    categories.append(new_category)

            book = Book.objects.create(
                title = row['title'],
                description = row['description'],
                url = row['url'],
                slug = slugify(row['title'])[:50]
            )

            for author in authors:
                book.authors.add(author)
            for category in categories:
                book.categories.add(category)


class Migration(migrations.Migration):

    dependencies = [
        ('shelf', '0001_initial'),
    ]

    operations = [migrations.RunPython(load_books)
    ]
