from django.urls import path
from quotes import views

app_name = 'quotes'

urlpatterns = [
    path('', views.main, name='root'),
    path('<int:page>', views.main, name='root_paginate'),
    path('author/add/', views.add_author, name='add_author'),
    path('quote/add/', views.add_quote, name='add_quote'),
    path('tag/<str:tag>/', views.quotes_by_tag, name='quotes_by_tag'),
]