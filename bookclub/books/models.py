from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    description = models.TextField()
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    cover_image = models.ImageField(upload_to='book_covers/', blank=True, null=True)    
    def __str__(self):
        return f"{self.title} by {self.author}"