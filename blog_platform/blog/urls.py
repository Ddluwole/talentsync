from django.urls import path
from .views import (
    CreateBlogPostView,
    ListBlogPostsView,
    RetrieveUpdateBlogPostView,
    DeleteBlogPostView,
    UserRegisterView,
    UserLoginView
)

urlpatterns = [
    path('blogposts/', ListBlogPostsView.as_view(), name='blogpost-list'),
    path('blogposts/create/', CreateBlogPostView.as_view(), name='blogpost-create'),
    path('blogposts/<int:pk>/', RetrieveUpdateBlogPostView.as_view(), name='blogpost-detail'),
    path('blogposts/<int:pk>/delete/', DeleteBlogPostView.as_view(), name='blogpost-delete'),
    path('register/', UserRegisterView.as_view(), name='user-register'),
    path('login/', UserLoginView.as_view(), name='user-login'),
]
