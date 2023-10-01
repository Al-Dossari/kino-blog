from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .models import Comments
from .form import CommentAddForm
from pages.models import Article

# Create your views here.



class CommentsCreateView(CreateView):
    model = Comments
    form_class = CommentAddForm
    template_name = 'article/article_detail.html'
    success_url = reverse_lazy('detail')


