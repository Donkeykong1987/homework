from django.urls import path
from .views import author_detail_views, entry_list_view, blog_detail_view
from .views import authors_list_view, search_list_view, authors_sorted

urlpatterns = [
    path('', entry_list_view, name='entry-list'),
    path('new_blog/<int:blog_id>/', blog_detail_view, name='blog-detail'),
    path('authors/', authors_list_view, name='author-list'),
    path('author_detail/<int:author_id>/', author_detail_views, name='author-details'),
    path('search/', search_list_view, name='search'),
    path('sorted/', authors_sorted, name='sorted'),
]