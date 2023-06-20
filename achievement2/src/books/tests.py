from django.test import TestCase
from .models import Book  # to access the Book model

# Create your tests here.


class BookModelTest(TestCase):
    def setUpTestData():
        Book.objects.create(name='Wild', author_name='Cheryl Strayed',
                            genre='educational', book_type='hardcover', price='25.03')

    def test_book_name(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_author_name_max_length(self):
        book = Book.objects.get(id=1)
        max_length = book._meta.get_field('author_name').max_length
        self.assertEqual(max_length, 120)
