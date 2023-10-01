from django.urls import path
from .views import category_view, index, ArticleView, ArticleDetail ,ArticleCreateView, ArticleUpdateView ,ArticleDeleteView





urlpatterns = [
    path('', ArticleView.as_view(), name='index'),
    path('category/<int:pk>', category_view, name='category'),
    path('article/<int:pk>', ArticleDetail.as_view(), name='detail'),
    path('article/add',ArticleCreateView.as_view(),name='article_add'),
    path('article/update/<int:pk>',ArticleUpdateView.as_view(),name='article_update'),
    path('article/delete/<int:pk>',ArticleDeleteView.as_view(),name='article_delete')
]
