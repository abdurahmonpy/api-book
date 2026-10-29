from django.urls import path
from .views import BookListAPIView, BookDetailAPIView, BookDetailBySlugAPIView

urlpatterns = [
    path('', BookListAPIView.as_view(), name='book-list'),
    path('<int:pk>/', BookDetailAPIView.as_view(), name='book-detail'),
    path('<slug:slug>/', BookDetailBySlugAPIView.as_view(), name='book-detail-slug'),
]
