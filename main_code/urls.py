from django.urls import path
from . import views

urlpatterns = [
    path('', views.leaderboard_view, name='leaderboard'),
    path('input/', views.input_skor_view, name='input_skor'),
]