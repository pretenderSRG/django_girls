from django.urls import path
from blog.views import post_list, post_detail

urlpatterns = [
    path('', post_list, name='home'),
    path('post/<int:pid>/', post_detail, name='post_detail'),
]