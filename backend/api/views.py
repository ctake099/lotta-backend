from rest_framework import viewsets
from .models import User, Book, UserBook
from .serializers import UserSerializer, BookSerializer, UserBookSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class UserBookViewSet(viewsets.ModelViewSet):
    queryset = UserBook.objects.all()
    serializer_class = UserBookSerializer
