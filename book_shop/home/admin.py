from django.contrib import admin
from .models import Book
# Register your models here.

class bookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'price')
    search_fields = ('id', 'title', 'author', 'price', 'description')
    list_filter = ('author', 'price')
    ordering = ('price', )

admin.site.register(Book, bookAdmin)