from django.db import models

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

class Book(models.Model):
    title = models.CharField(max_length=155)
    author = models.CharField(max_length=100)
    caption = models.TextField()
    publication_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class UserBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    book_memo = models.TextField(blank=True, null=True)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'book') 

    def __str__(self):
        return f'{self.user.username} - {self.book.title}'
