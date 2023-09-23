from django.shortcuts import render,redirect
from .models import *
from .forms import *

def index(request):
    context = {
        'categories': Category.objects.all(),
        'books': Book.objects.all(),
        'form': BookForm(),
        'formcat': CategoryForm(),
        'allbookcont': Book.objects.all().count(),
        'booksold': Book.objects.filter(status='sold').count(),
        'bookavailable': Book.objects.filter(status='available').count(),
        'bookrent': Book.objects.filter(status='rented').count(),
    }

    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        add_cat = CategoryForm(request.POST)
        if add_cat.is_valid():
            add_cat.save()
    
    return render(request, 'page/index.html', context)

def book(request):
    title = request.GET.get("search_name", None)
    books = Book.objects.filter(title__icontains=title) if title else Book.objects.all()
    
    context = {'categories': Category.objects.all(), 'books': books , 'formcat': CategoryForm(),}
    
    return render(request, 'page/books.html', context)


def update(request, id):
    book_id = Book.objects.get(id=id)
    next_page = request.GET.get('next', 'index')
    form = BookForm(instance=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST,request.FILES ,instance=book_id)
        if form.is_valid():
            form.save()
            if next_page == 'book':
                return redirect('book')
            else:
                return redirect('index')
    else:
        form = BookForm(instance=book_id)
    context = {
        'form': form,
    }

    
    return render(request, 'page/update.html', context)

def delete(request, id):
    book_id = Book.objects.get(id=id)
    next_page = request.GET.get('next', 'index')
    if request.method == 'POST':
        book_id.delete()
        if next_page == 'book':
            return redirect('book')  
        else:
            return redirect('index')
    context = {
        'book_id': book_id,
    }
    return render(request, 'page/delete.html', context)