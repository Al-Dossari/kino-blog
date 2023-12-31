from django.contrib import admin
from .models import Comments


# Register your models here.
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('article', 'author', 'context', 'created_at')


admin.site.register(Comments, CommentsAdmin)
