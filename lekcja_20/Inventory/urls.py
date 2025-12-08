from django.urls import path
from . import views

urlpatterns = [
    path('info/', views.info, name='info'),
    path('rules/', views.rules, name='rules'),
    path('user/<str:username>/', views.user_profile, 
    name='user_profil'),
    path('category/<int:category_id>/', views.category_products, 
    name='category_products')
]