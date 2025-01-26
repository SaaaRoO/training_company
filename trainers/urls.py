from django.urls import path
from .views import TrainerListView, TrainerCreateView, TrainerUpdateView, TrainerDeleteView

urlpatterns = [
    path('', TrainerListView.as_view(), name='trainer-list'),
    path('new/', TrainerCreateView.as_view(), name='trainer-create'),
    path('<int:pk>/edit/', TrainerUpdateView.as_view(), name='trainer-update'),
    path('<int:pk>/delete/', TrainerDeleteView.as_view(), name='trainer-delete'),
]