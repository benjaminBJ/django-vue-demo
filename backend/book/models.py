from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=50)
    
    def __str__(self):
        return self.title

class Page(models.Model):
    number = models.IntegerField()
    content = models.TextField()
    book = models.ForeignKey(
        Book, 
        on_delete=models.CASCADE, 
        related_name='pages')
    def __str__(self):
        return f"Page {self.number} - {self.book}"

