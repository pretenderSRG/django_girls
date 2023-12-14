from django.urls import path
from blog.views import post_list, post_detail, post_new, post_edit, post_delete

urlpatterns = [
    path('', post_list, name='home'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('post/new/', post_new, name='post_new'),
    path('post/<int:pk>/edit/', post_edit, name='post_edit'),
    path('post/<int:pk>/delete/', post_delete, name='post_delete'),
]