from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from django.shortcuts import render, redirect, get_object_or_404

from Myapp.models import Books
from Myapp.my_forms import BookForm, RegisterForm


# Create your views here.
@login_required
def show_books(request):
    books = Books.objects.all() #select * from books
    return render(request, 'show_books.html', {'books': books})

@login_required
@permission_required('Myapp.add_book',raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST,request.FILES)
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
@login_required
@permission_required('Myapp.delete_book')
def delete_book(request,id):
    book = Books.objects.get(id=id) #select * from books where id = 34
    book.delete() #delete from books where id = 34
    messages.warning(request, f'{book.title} Deleted Successfully')
    return redirect('show_books')


@login_required
@permission_required('Myapp.change_book',raise_exception=True)
def edit_book(request,id):
    book = get_object_or_404(Books,pk=id)
    if request.method == 'POST':
        form = BookForm(request.POST,request.FILES, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, f'{book.title} Updated Successfully')
            return redirect('show_books')
    else:
        form = BookForm(instance=book)
    return render(request, 'edit_book.html', {'form': form})


def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('show_books')
    else:
        form = AuthenticationForm()
    return render(request,'registration/login.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')
    else:
        form = AuthenticationForm()
    return render(request,'registration/signup.html', {'form': form})


@login_required
def signout(request):
    if request.method == 'POST':
        login(request)
    return redirect('login')