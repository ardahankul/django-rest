from django.urls import path
from .views import FavoriteCreateAPIView,FavoriteListAPIView,FavoriteDeleteAPIView

app_name = "favorite"

urlpatterns = [
    path('create/', FavoriteCreateAPIView.as_view(), name='create'),
    path('list/',FavoriteListAPIView.as_view(), name = 'list'),
    path('delete/<pk>',FavoriteDeleteAPIView.as_view(), name='delete'),  
]