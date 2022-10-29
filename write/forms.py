from django import forms
from django_summernote.fields import SummernoteTextField
from .models import Book, Chapter, Notes


class BookForm(forms.ModelForm):
    synopsis = SummernoteTextField()

    class Meta:
        model = Book
        fields = ['title', 'subtitle', 'genre', 'synopsis', 'status']


class ChapterForm(forms.ModelForm):
    content = SummernoteTextField()

    class Meta:
        model = Chapter
        fields = ['title', 'subtitle', 'content', 'status']


class NotesForm(forms.ModelForm):
    content = SummernoteTextField()

    class Meta:
        model = Notes
        fields = ['content']
