from . import views
from django.urls import path
from .views import PostDetail, AddPost, EditPost


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('addpost/', AddPost.as_view(), name='add_post'),
    path('editpost/<slug:pk>/', EditPost.as_view(), name='edit_post'),
    path('post_detail/<slug:slug>/',
         views.PostDetail.as_view(), name='post_detail'),
]
