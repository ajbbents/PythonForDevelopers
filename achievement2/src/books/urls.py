from django.urls import path
from .views import BookListView

app_name = 'books'

urlpatterns = [
    path('list/', BookListView.as_view(), name='list')
]
