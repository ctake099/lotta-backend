from rest_framework import serializers # type: ignore
from .models import User, Book, UserBook

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'created_at']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # パスワードのハッシュ化を行う
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
        )
        return user

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'caption', 'publication_date', 'isbn', 'created_at']

class UserBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBook
        fields = ['id', 'user', 'book', 'book_memo', 'added_at']
        read_only_fields = ['user', 'book', 'added_at']

