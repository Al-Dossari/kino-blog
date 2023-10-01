from django.urls import path
from .views import CommentsCreateView

urlpatterns = [
    path('add/', CommentsCreateView.as_view(), name='comments_add'),



]
