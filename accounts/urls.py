from django.urls import path
from .views import SignUpView ,ProfileView , EditView


urlpatterns = [
    path('signup/',SignUpView.as_view(),name='signup'),
    path('',ProfileView.as_view(),name='profile'),
    path('edit/<int:pk>/',EditView.as_view(),name='edit')

]