from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

from .models import Article, Category
from django.views.generic import ListView, DeleteView, DetailView, UpdateView, CreateView
from .forms import ArticleForm


# Create your views here.


def index(request):
    articles = Article.objects.all()
    context = {
        'title': 'Киномания',
        'article': articles
    }
    return render(request, 'index.html', context)


class ArticleView(ListView):
    model = Article
    template_name = 'index.html'
    context_object_name = 'articles'


def category_view(request, pk):
    articles = Article.objects.filter(category_id=pk)
    category = Category.objects.get(pk=pk)

    context = {
        'title': f'Категория {category.title}',
        'articles': articles
    }

    return render(request, 'index.html', context)


def article_view(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'title': f'Статья :{article.title}',
        'article': article
    }
    return render(request, 'article/article_detail.html', context)


class ArticleDetail(DetailView):
    model = Article
    template_name = 'article/article_detail.html'


class ArticleUpdateView(UpdateView, LoginRequiredMixin, UserPassesTestMixin):
    model = Article
    template_name = 'article/article_form.html'
    form_class = ArticleForm

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleCreateView(CreateView, LoginRequiredMixin, UserPassesTestMixin):
    model = Article
    template_name = 'article/article_form.html'
    form_class = ArticleForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ArticleDeleteView(DeleteView, LoginRequiredMixin, UserPassesTestMixin):
    model = Article
    template_name = 'article/article_delete.html'
    success_url = reverse_lazy('index')

    # user superuser ekanini tekshirish
    def test_func(self):
        return self.request.user.is_superuser
