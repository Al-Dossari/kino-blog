from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields  = ('title','produce_date','original_name','content','category','photo','video')

        widgets = {
            'title': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': "Название статьи"
            }),
            'original_name': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': "Оригиналное название"
            }),
            'content': forms.Textarea(attrs={
                'class': "form-control",
                'placeholder': "Содержимое статьи"
            }),
            'photo': forms.FileInput(attrs={
                'class': "form-control"
            }),
            'video': forms.FileInput(attrs={
                'class': "form-control"
            }),
            'category': forms.Select(attrs={
                'class': "form-control"
            }),
            'produce_date' : forms.DateInput(attrs={
                'class' :'form-control',
                'place-holder' : 'Дата'
            })

        }




