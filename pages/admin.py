from django.contrib import admin
from .models import Article, Category

# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','original_name','produce_date','author','category')


admin.site.register(Category)
admin.site.register(Article,ArticleAdmin)

