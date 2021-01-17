from django.contrib import admin

from word_memorization.models import Category
from word_memorization.models import Word

admin.site.register(Category)
admin.site.register(Word)