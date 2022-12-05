from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='home'),
    path("", views.PostList.as_view(), name="home"),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('create_post', views.create_post, name='create_post'),
    path('profile', views.profile, name='profile'),
    path('my_posts', views.my_posts, name='my_posts'),
    path('edit/<post_id>', views.edit_post, name='edit'),
    path('delete/<post_id>', views.delete_post, name='delete_post'),
]