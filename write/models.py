import re
from django.db import models
from accounts.models import Account
from django.utils.text import slugify

STATUS = ((0, 'Draft'), (1, 'Published'))


class Book(models.Model):
    creator = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=80, unique=True)
    subtitle = models.CharField(max_length=120, null=True, blank=True)
    slug = models.SlugField(max_length=80, unique=True)
    genre = models.CharField(max_length=80, null=True, blank=True)
    synopsis = models.TextField(blank=True)
    created_on = models.DateField(auto_now_add=True)
    edited_on = models.DateField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-status', '-created_on']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Book, self).save(*args, **kwargs)


class Chapter(models.Model):
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True, related_name='chapter')
    title = models.CharField(max_length=40)
    subtitle = models.CharField(max_length=80, null=True, blank=True)
    slug = models.SlugField(max_length=40, unique=True)
    content = models.TextField()
    wordcount = models.IntegerField(default=0)
    created_on = models.DateField(auto_now_add=True)
    edited_on = models.DateField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['created_on']
        get_latest_by = ['created_on']
    
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        text = re.sub(r'<.*?>', ' ', self.content)
        self.wordcount = len(text.split())
        self.slug = '-'.join((slugify(self.book.slug), slugify(self.title)))
        super(Chapter, self).save(*args, **kwargs)


class Notes(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.SET_NULL, null=True, related_name='notes')
    content = models.TextField()
    created_on = models.DateField(auto_now_add=True)
    edited_on = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-edited_on']

    def __str__(self):
        return f'Notes for {self.chapter}'
