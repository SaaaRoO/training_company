from django.urls import path
from .views import CourseListView, CourseCreateView, CourseUpdateView, CourseDeleteView

urlpatterns = [
    path('', CourseListView.as_view(), name='course-list'),
    path('new/', CourseCreateView.as_view(), name='course-create'),
    path('<int:pk>/edit/', CourseUpdateView.as_view(), name='course-update'),
    path('<int:pk>/delete/', CourseDeleteView.as_view(), name='course-delete'),
]