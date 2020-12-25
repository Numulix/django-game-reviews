from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('game/<int:id>/', views.detail, name='detail'),
    path('addgame/', views.add_game, name='add_game'),
    path('editgame/<int:id>/', views.edit_game, name='edit_game'),
    path('deletegame/<int:id>/', views.delete_game, name='delete_game')
]