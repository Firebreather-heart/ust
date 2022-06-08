from .views import (
    display,search_product,
    ArticleCreateView,
    ArticleDeleteView,
    ArticleUpdateView,
    CommentView,
    ArticleDetailView,
    )
from django.urls import path 

urlpatterns = [
    path('',display,name='home'),
    path('create/',ArticleCreateView.as_view(),name='article_create'),
    path('<uuid:pk>/delete/',ArticleDeleteView.as_view(),name='article_delete'),
    path('<uuid:pk>/edit/',ArticleUpdateView.as_view(),name='article_update'),
    path('<uuid:pk>/comment/',CommentView.as_view(),name='comment'),
    path('search/',search_product,name='search'),
    path('<uuid:pk>/detail',ArticleDetailView.as_view(),name='article_detail')
]