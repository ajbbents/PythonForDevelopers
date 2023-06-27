from django.shortcuts import render  # default import
from django.views.generic import ListView, DetailView  # to display lists, details
from .models import Book  # access Book model
# to protect class-based view
from django.contrib.auth.mixins import LoginRequiredMixin


class BookListView(LoginRequiredMixin, ListView):  # CBV
    model = Book  # specifying model
    template_name = 'books\main.html'  # specifying template


class BookDetailView(LoginRequiredMixin, DetailView):  # CBV
    model = Book  # specifying model again
    template_name = 'books\detail.html'  # specifying template again
