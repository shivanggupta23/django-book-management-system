from django.http import HttpResponse
from django.shortcuts import render,redirect

from books.models import Book

from django.shortcuts import render, redirect,get_object_or_404
from .models import Book
from .forms import BookForm

# Create your views here.

def home(request):
    context={
        "message":"welcome to the book store!"
    }
    return render(request,"books/home.html",context)

def book_list(request):
    books=Book.objects.all()
    
    context={
        "books":books
    }
    return render(request,"books/book_list.html",context)

def add_book(request):
    if request.method == "POST":
        title = request.POST["title"]
        author = request.POST["author"]
        price = request.POST["price"]
        published_date = request.POST["published_date"]

        Book.objects.create(
            title=title,
            author=author,
            price=price,
            published_date=published_date
        )

        return redirect("book_list")

    return render(request, "books/add_book.html")

def book_detail(request,id):
    book=get_object_or_404(Book,id=id)
    
    return render(request,"books/book_detail.html",{"book":book})


def edit_book(request, id):
    book = get_object_or_404(Book,id=id)

    if request.method == "POST":
        book.title = request.POST["title"]
        book.author = request.POST["author"]
        book.price = request.POST["price"]
        book.published_date = request.POST["published_date"]

        book.save()

        return redirect("book_detail", id=book.id)

    return render(request, "books/edit_book.html", {"book": book})

def delete_book(request,id):
    book=get_object_or_404(Book,id=id)
    
    if request.method=="POST":
        book.delete()
        return redirect("book_list")
    
    return render(request,"books/delete_book.html",{"book":book})
