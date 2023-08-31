from . import views
from django.urls import path
from .views import PostDetail, AddPost, EditPost, DeletePost, AboutView
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('addpost/', AddPost.as_view(), name='add_post'),
    path('editpost/<slug:pk>/', EditPost.as_view(), name='edit_post'),
    path('deletepost/<slug:pk>/delete',
         DeletePost.as_view(), name='delete_post'),
    path('post_detail/<slug:slug>/',
         views.PostDetail.as_view(), name='post_detail'),
    path('post_reserved/<slug:slug>/reserve',
         views.Reserve_Food_Item.as_view(), name='post_reserved'),
    path('about/', views.AboutView.as_view(), name='about'),
]
