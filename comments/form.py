from django import forms
from .models import Comments


class CommentAddForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('context',)
        context = forms.CharField(widget=forms.TextInput(attrs={
            'class' : 'form-control',
            'placeholder' : 'Комментария'
        }))