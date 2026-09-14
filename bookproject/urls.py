"""
URL configuration for bookproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from books.views import home
from books.views import book_list
from books.views import add_book,book_detail,edit_book,delete_book

urlpatterns = [
    path('',home),
    path('books/',book_list,name='book_list'),
    path('books/add/',add_book,name='add_book'),
    path('books/<int:id>/',book_detail,name='book_detail'),
    path('books/<int:id>/edit/',edit_book,name='edit_book'),
    path('books/<int:id>/delete/',delete_book,name='delete_book'),
    path("admin/", admin.site.urls),
    ]

