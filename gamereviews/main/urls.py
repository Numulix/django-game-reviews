from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('game/<int:id>/', views.detail, name='detail'),
    path('addgame/', views.add_game, name='add_game')
]