from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            'id',
            'title',
            'slug',
            'pdf',
            'image',
            'created_at',
        ]
        read_only_fields = ['id', 'slug', 'created_at']
