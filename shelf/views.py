from django.shortcuts import render
from shelf.models import Book, Category

def index(request):
    """View function for home page of site."""

    books = Book.objects.all()
    categories = Category.objects.all()
    
    context = {
        'books': books,
        'categories': categories,
    }

    return render(request, 'index.html', context=context)

def category_list_view(request, pk):
    category = Category.objects.get(pk=pk)
    categories = Category.objects.all()
    books_in_category = [book for book in Book.objects.all() if category in book.categories.all()]

    return render(request, 'category_list.html', {
        'books_in_category': books_in_category,
        'categories': categories,
        })
