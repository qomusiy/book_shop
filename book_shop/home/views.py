from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from django.views.generic import View
from django.db.models import Q
from .forms import BookForm
# Create your views here.

class Home(View):
    def get(self, r):
        query = r.GET.get('t', '')
        books = Book.objects.filter(Q(title__icontains=query)|Q(author__icontains=query)|Q(genre__icontains=query))
        return render(r, template_name='home.html', context={'book':books})

def about(r):
    return render(r, template_name='about.html')

def contact(r):
    return render(r, template_name='contact.html')

class InfoBook(View):
    def get(self, r, pk):
        return render(r, template_name='infobook.html', context={'book':get_object_or_404(Book, pk=pk)})
    
# class SearchBook(View):
#     def get(self, r):
#         query = r.GET.get('t', '.')
#         books = Book.objects.filter(title__icontains=query)
#         return render(r, template_name='search.html', context={'books':books})


class AddBook(View):
    def get(self, r):
        return render(r, template_name='addbook.html', context={'form': BookForm()})
    
    def post(self, r):
        form = BookForm(r.POST, r.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(r, template_name='addbook.html', context={'form':form})
    
class EditBook(View):
    def get(self, r, pk):
        book = get_object_or_404(Book, pk=pk)
        form = BookForm(instance=book)
        return render(r, 'addbook.html', {'form': form, 'book': book})

    def post(self, r, pk):
        book = get_object_or_404(Book, pk=pk)
        form = BookForm(r.POST, r.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(r, 'addbook.html', {'form': form, 'book': book})
    
class DeleteBook(View):
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        return render(request, 'delete.html', {'book': book})

    def post(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        book.delete()
        return redirect('home')