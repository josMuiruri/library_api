from django.test import TestCase
from django.urls import reverse
from .models import Book

# Create your tests here.
class BookTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.book = Book.objects.create(
            title='Great title',
            subtitle='good subtitle',
            author='Author lee',
            isbn='1234567890123',
        )

    def test_book_content(self):
        self.assertEqual(self.book.title, 'Great title')
        self.assertEqual(self.book.subtitle, 'good subtitle')
        self.assertEqual(self.book.author, 'Author lee')
        self.assertEqual(self.book.isbn, '1234567890123')

    def test_book_listview(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'good subtitle')
        self.assertTemplateUsed(response, 'books/book_list.html')