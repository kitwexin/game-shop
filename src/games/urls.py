from django.urls import path
from . import views
app_name = 'games'

urlpatterns = [
    path('create-game/', views.GamesCreateView.as_view(), name = 'create'),
    path('list-games/', views.GamesListView.as_view(), name = 'list'),
    path('update-game/<int:pk>', views.GamesUpdateView.as_view(), name = 'update'),
    path('delete-game/<int:pk>', views.GamesDeleteView.as_view(), name = 'delete'),
    path('game/<int:pk>', views.GamesDetailView.as_view(), name = 'detail')
]