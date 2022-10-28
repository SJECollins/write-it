from django.contrib import admin
from .models import Book, Chapter, Notes


admin.site.register(Book)
admin.site.register(Chapter)
admin.site.register(Notes)
