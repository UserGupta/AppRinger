from django.contrib import admin
from django.urls import path, include
from booksStore import views

urlpatterns = [
    path("", views.index, name="booksStore"),
]
