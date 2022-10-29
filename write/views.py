from django.shortcuts import render, get_object_or_404, redirect

from .models import Book, Chapter, Notes
from .forms import BookForm, ChapterForm, NotesForm


def home(request):
    """ Home view, list of books """
    book_list = Book.objects.all()
    paginator = Paginator(book_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    template_name = 'write/index.html'
    context = {
        'book_list': book_list,
        'page_obj': page_obj,
        }
    return render(request, template_name, context)


def book(request, slug):
    book = get_object_or_404(Book, slug=slug)
    chapters = book.chapter.all()
    template_name = 'write/book.html'
    context = {
        'book': book,
        'chapters': chapters,
    }
    return render(request, template_name, context)


def chapter(request, slug):
    chapter = get_object_or_404(Chapter, slug=slug)
    notes = chapter.notes.all()
    template_name = 'write/chapter.html'
    context = {
        'chapter': chapter,
        'notes': notes,
    }
    return render(request, template_name, context)


def add_book(request):
    template_name = 'write/book_form.html'
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.creator = request.user
            instance.save()
            return redirect('write:home')
    else:
        form = BookForm()
    context = {
        'form': form,
    }
    return render(request, template_name, context)


def edit_book(request, slug):
    book = get_object_or_404(Book, slug=slug)
    template_name = 'write/book_form.html'
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('write:home')
    else:
        form = BookForm(request.POST or None, instance=book)
    context = {
        'book': book,
        'form': form,
    }
    return render(request, template_name, context)


def add_chapter(request, slug):
    book = get_object_or_404(Book, slug=slug)
    template_name = 'write/chapter_form.html'
    if request.method == 'POST':
        form = ChapterForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            try:
                book = Book.objects.get(slug=slug)
            except Book.DoesNotExist:
                pass
            instance.book = book
            instance.save()
            return redirect('write:home')
    else:
        form = ChapterForm()
    context = {
        'book': book,
        'form': form,
    }
    return render(request, template_name, context)


def edit_chapter(request, slug):
    chapter = get_object_or_404(chapter, slug=slug)
    template_name = 'write/chapter_form.html'
    form = ChapterForm(request.POST or None, instance=chapter)
    if form.is_valid():
        form.save()
        return redirect('write:home')
    else:
        form = ChapterForm(request.POST or None, instance=chapter)
    context = {
        'chapter': chapter,
        'form': form,
    }
    return render(request, template_name, context)


def add_notes(request, slug):
    chapter = get_object_or_404(Chapter, slug=slug)
    template_name = 'write/notes_form.html'
    if request.method == 'POST':
        form = NotesForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            try:
                chapter = Chapter.objects.get(slug=slug)
            except Chapter.DoesNotExist:
                pass
            instance.chapter = chapter
            instance.save()
            return redirect('write:home')
    else:
        form = NotesForm()
    context = {
        'chapter': chapter,
        'form': form,
    }
    return render(request, template_name, context)


def edit_notes(request, note_id):
    notes = get_object_or_404(Notes, id=note_id)
    template_name = 'write/notes_form.html'
    form = NotesForm(request.POST or None, instance=notes)
    if form.is_valid():
        form.save()
        return redirect('write:home')
    else:
        form = NotesForm(request.POST or None, instance=notes)
    context = {
        'notes': notes,
        'form': form,
    }
    return render(request, template_name, context)
