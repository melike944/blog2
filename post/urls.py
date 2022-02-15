from.views import post
from django.urls import path
urlpatterns = [
    path('', post,name="post"),
]
