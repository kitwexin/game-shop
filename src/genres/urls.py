from django.urls import path
from . import views
app_name = 'genres'

urlpatterns = [
    path('create-genre/', views.GenresCreateView.as_view(), name = 'create'),
    path('list-genres/', views.GenresListView.as_view(), name = 'list'),
    path('update-genre/<int:pk>', views.GenresUpdateView.as_view(), name = 'update'),
    path('delete-genre/<int:pk>', views.GenresDeleteView.as_view(), name = 'delete'),
    path('genre/<int:pk>', views.GenresDetailView.as_view(), name = 'detail')
]