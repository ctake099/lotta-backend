from django.contrib import admin
from .models import Book, User, UserBook 

# モデルを管理サイトに登録
admin.site.register(Book)
admin.site.register(User)
admin.site.register(UserBook)