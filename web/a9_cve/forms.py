from django import forms
from django.forms import Form


class BooksForm(Form):
    path_to_book = forms.CharField(
        label='Select book',
        widget=forms.Select(
            choices=[('/books/lorem.txt',            'Lorem Ipsum'),
                     ('/books/1984.txt',             'George Orwell - 1984'),
                     ('/books/romeo_and_juliet.txt', 'William Shakespeare: Romeo and Juliet')]
        )
    )
