from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberInternationalFallbackWidget
from .models import CustomUser
from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = (
            'username', 'first_name', 'last_name', 'email', 'age', 'phone_number', 'photo', 'address', 'password1',
            'password2')

    username = forms.CharField(max_length=50,
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control',
                                   'placeholder': 'username'
                               }))

    first_name = forms.CharField(max_length=50,
                                 widget=forms.TextInput(attrs={
                                     'class': 'form-control',
                                     'placeholder': 'Имя'
                                 }))
    last_name = forms.CharField(max_length=50,
                                widget=forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Фамилия'
                                }))

    email = forms.EmailField(max_length=50,
                             widget=forms.EmailInput(attrs={
                                 'class': 'form-control',
                                 'placeholder': 'email'
                             }))

    age = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': "form-control",
        'placeholder': 'age'
    }))
    phone_number = PhoneNumberField(widget=PhoneNumberInternationalFallbackWidget(attrs={
        'class': 'form-control',
        'placeholder': 'Телефон'
    }))
    address = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Адрес'
    }))
    photo = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'form-control',
        'placeholder': 'Фотография'
    }))

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Пароль'
        }))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Повторите Пароль'
        }))


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'age', 'phone_number', 'photo', 'address','password1','password2')

    username = forms.CharField(max_length=50,
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control',
                                   'placeholder': 'username'
                               }))

    first_name = forms.CharField(max_length=50,
                                 widget=forms.TextInput(attrs={
                                     'class': 'form-control',
                                     'placeholder': 'Имя'
                                 }))
    last_name = forms.CharField(max_length=50,
                                widget=forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Фамилия'
                                }))

    email = forms.EmailField(max_length=50,
                             widget=forms.EmailInput(attrs={
                                 'class': 'form-control',
                                 'placeholder': 'email'
                             }))

    age = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': "form-control",
        'placeholder': 'age'
    }))
    phone_number = PhoneNumberField(widget=PhoneNumberInternationalFallbackWidget(attrs={
        'class': 'form-control',
        'placeholder': 'Телефон'
    }))
    address = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Адрес'
    }))
    photo = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'form-control',
        'placeholder': 'Фотография'
    }))
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Пароль'
        }))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Повторите Пароль'
        }))
