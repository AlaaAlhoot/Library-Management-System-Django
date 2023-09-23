from django.urls import path,include 
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('book/', views.book, name='book'),
    path('<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
]
