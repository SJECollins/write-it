from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('book/<slug:slug>', views.book, name='book'),
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<slug:slug>', views.edit_book, name='edit_book'),
    path('chapter/<slug:slug>', views.chapter, name='chapter'),
    path('add_chapter/<slug:slug>', views.add_chapter, name='add_chapter'),
    path('edit_chapter/<slug:slug>', views.edit_chapter, name='edit_chapter'),
    path('add_note/<slug:slug>', views.add_notes, name='add_note'),
    path('edit_note/<note_id>', views.edit_notes, name='edit_note'),
]