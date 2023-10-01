from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=200,
                             unique=True,
                             verbose_name='Название категории')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=255,
                             verbose_name='Название статьи')
    produce_date = models.DateField('Год производства', max_length=255)
    original_name = models.CharField(max_length=255, verbose_name='оригинальное название')
    content = models.TextField(verbose_name='Описание статьи')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='Автор')
    photo = models.ImageField(upload_to='articles/', null=True, blank=True, verbose_name='Фотография')
    video = models.FileField(upload_to='videos/', null=True, blank=True, verbose_name='Видео')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


