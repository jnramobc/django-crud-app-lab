from django.urls import path
from . import views

urlpatterns = [
    path('', views.BirdList.as_view(), name='bird-index'),  # Index/List
    path('<int:pk>/', views.BirdDetail.as_view(), name='bird-detail'),  # Detail
    path('create/', views.BirdCreate.as_view(), name='bird-create'),  # Create
    path('<int:pk>/update/', views.BirdUpdate.as_view(), name='bird-update'),  # Update
    path('<int:pk>/delete/', views.BirdDelete.as_view(), name='bird-delete'),  # Delete
    path('<int:pk>/add-sighting/', views.SightingCreate.as_view(), name='add-sighting'),
]
