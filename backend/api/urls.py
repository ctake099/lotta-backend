from django.urls import path, include
from rest_framework.routers import DefaultRouter # type: ignore
from .views import UserViewSet, BookViewSet, UserBookViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'books', BookViewSet)
router.register(r'userbooks', UserBookViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
