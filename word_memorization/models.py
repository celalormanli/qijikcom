from django.db import models

# Create your models here.

class Category(models.Model):
    category_name=models.CharField(max_length=100, blank=False, default='', primary_key=True)



class Word(models.Model):
    english=models.CharField(max_length=100, blank=False, default='')
    turkish=models.CharField(max_length=100, blank=False, default='')
    german=models.CharField(max_length=100, blank=False, default='')
    french=models.CharField(max_length=100, blank=False, default='')
    category_name=models.ForeignKey(Category, on_delete=models.CASCADE)