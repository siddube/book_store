from django.shortcuts import get_object_or_404, render
from .models import Book
# Create your views here.

def index(request):
  book = Book.objects.all()
  
  return render(request, 'book_outlet/index.html', {'books': book})

def book_detail(request, slug):
  book = get_object_or_404(Book, slug=slug)
  return render(request, 'book_outlet/book_detail.html', {'book': book}) 