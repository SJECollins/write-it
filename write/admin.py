from django.contrib import admin
from .models import Book, Chapter, Notes

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'creator', 'created_on', 'edited_on', 'status')
    list_filter = ('title', 'created_on', 'status')
    search_fields = ('title', 'genre',)


class ChapterAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_on', 'edited_on', 'status')
    list_filter = ('created_on', 'status')


admin.site.register(Book, BookAdmin)
admin.site.register(Chapter, ChapterAdmin)
admin.site.register(Notes)
