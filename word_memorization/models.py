from django.db import models

# Create your models here.

class Category(models.Model):
    category_name=models.CharField(max_length=100, blank=False, default='')



class Word(models.Model):
    english=models.CharField(max_length=100, blank=False, default=100)
    turkish=models.CharField(max_length=100, blank=False, default=100)
    german=models.CharField(max_length=100, blank=False, default=100)
    french=models.CharField(max_length=100, blank=False, default=100)
    category_name=models.ForeignKey(Category, on_delete=models.CASCADE)