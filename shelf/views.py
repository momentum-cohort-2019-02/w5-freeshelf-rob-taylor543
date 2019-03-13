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
    pass
