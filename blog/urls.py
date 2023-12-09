from django.urls import path
from blog.views import post_list

urlpatterns = [
    path('post/', post_list),
]