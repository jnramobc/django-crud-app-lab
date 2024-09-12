from django.urls import path
from . import views

urlpatterns = [
    path('', views.BirdList.as_view(), name='bird_list'),  # Index/List
    path('<int:pk>/', views.BirdDetail.as_view(), name='bird-detail'),  # Detail
    path('create/', views.BirdCreate.as_view(), name='bird-create'),  # Create
    path('<int:pk>/update/', views.BirdUpdate.as_view(), name='bird-update'),  # Update
    path('<int:pk>/delete/', views.BirdDelete.as_view(), name='bird-delete'),  # Delete
    path('<int:pk>/add-sighting/', views.SightingCreate.as_view(), name='add-sighting'),

        # Sighting CRUD
    path('sightings/', views.SightingList.as_view(), name='sighting-list'),
    path('sightings/<int:pk>/', views.SightingDetail.as_view(), name='sighting-detail'),
    path('sightings/<int:pk>/update/', views.SightingUpdate.as_view(), name='sighting-update'),
    path('sightings/<int:pk>/delete/', views.SightingDelete.as_view(), name='sighting-delete'),
    path('accounts/signup/', views.SignUpView.as_view(), name='signup'), 
]
