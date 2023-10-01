from django.contrib.auth import get_user_model
from django.db import models

from pages.models import Article


# Create your models here.


class Comments(models.Model):
    context = models.TextField(verbose_name='Комментария')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='author')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.article}: {self.context}'

    class Meta:
        verbose_name = 'Комментария'
        verbose_name_plural = 'Комментарии'
