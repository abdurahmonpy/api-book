from rest_framework import generics
from drf_spectacular.utils import extend_schema
from .models import Book
from .serializers import BookSerializer


@extend_schema(
    summary="Barcha kitoblar ro'yxati yoki yangi kitob qo'shish",
    description="Kitoblar ro'yxatini (id, title, slug, pdf, rasm, qo'shilgan vaqti) olish yoki yangi kitob yaratish.",
)
class BookListAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


@extend_schema(
    summary="Bitta kitobni ID orqali ko'rish, yangilash yoki o'chirish",
    description="Berilgan ID bo'yicha bitta kitob tafsilotlarini ko'rish yoki tahrirlash.",
)
class BookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


@extend_schema(
    summary="Bitta kitobni SLUG orqali ko'rish, yangilash yoki o'chirish",
    description="Berilgan slug (masalan: 'otkan-kunlar') bo'yicha bitta kitob tafsilotlarini ko'rish.",
)
class BookDetailBySlugAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'slug'
