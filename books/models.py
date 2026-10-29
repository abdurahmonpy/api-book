from django.db import models
from django.utils.text import slugify


class Book(models.Model):
    title = models.CharField(max_length=255, verbose_name="Kitob nomi")
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True, verbose_name="Slug")
    pdf = models.FileField(upload_to='books/pdfs/', blank=True, null=True, verbose_name="PDF fayli")
    image = models.ImageField(upload_to='books/images/', blank=True, null=True, verbose_name="Kitob rasmi")
    author = models.CharField(max_length=150, blank=True, null=True, verbose_name="Muallif")
    description = models.TextField(blank=True, null=True, verbose_name="Tavsif")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Qo'shilgan vaqti")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Yangilangan vaqti")

    class Meta:
        verbose_name = "Kitob"
        verbose_name_plural = "Kitoblar"
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            if not base_slug:
                base_slug = "kitob"
            slug = base_slug
            counter = 1
            while Book.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
