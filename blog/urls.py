from django.urls import path
from . import views
from .views import (
    PostListView,
    PostDetailView,
    CategoryView,
    BlogPostListView,
)


urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('about/', views.about, name='about'),
    #path('post-list/', BlogPostListView.as_view(), name='list'),
    path('post-list', BlogPostListView.as_view(), name='list'),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('blog-post/<int:pk>/', PostDetailView.as_view(), name='single'),
]