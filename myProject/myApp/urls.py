from django.urls import path
from .views import *


urlpatterns = [
    path('',loginPage, name='login'),
    path('signupPage/',signupPage, name='signupPage'),
    path('home/',home, name='home'),
    path('delete/<int:id>', dele, name='delete'),
    path('edit/<int:id>',edit, name='edit'),
     path('add', add, name='add'),
]
