from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('add/', views.add_book, name='add_book'), 
    #path('edit/<int:book_id>/', views.edit_book, name='edit_book'),
    #path('<int:book_id>/', views.book_detail, name='book_detail'),
]