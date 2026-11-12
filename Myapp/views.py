from django.shortcuts import render, redirect, get_object_or_404

from Myapp.models import Books
from Myapp.my_forms import BookForm


# Create your views here.
def show_books(request):
    books = Books.objects.all() #select * from books
    return render(request, 'show_books.html', {'books': books})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_books')
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})

# Books.objects.create(title='River and the Source',
    #                      year=2021,
    #                      category='Fiction',
    #                      cost='350',
    #                      isbn='4333444555757',
    #                      published = True)
    # Books.objects.create(title='River and the Source',
    #                      year=2020,
    #                      category='Fiction',
    #                      cost='350',
    #                      isbn='4333444555757',
    #                      published=True)
#              delete_book/34
def delete_book(request,id):
    book = Books.objects.get(id=id) #select * from books where id = 34
    book.delete() #delete from books where id = 34
    return redirect('show_books')


def edit_book(request,id):
    book = get_object_or_404(Books,pk=id)
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_books')
    else:
        form = BookForm(instance=book)
    return render(request, 'add_book.html', {'form': form})
