# importing django routing libraries
from django.urls import path

from . import views

urlpatterns = [
    # home page
    path('', views.PostsList.as_view(), name='posts'),
    # route for posts
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
