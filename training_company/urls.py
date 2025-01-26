from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView  # Add this import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('courses/', include('courses.urls')),
    path('trainers/', include('trainers.urls')),
    path('payments/', include('payments.urls')),
    path('', RedirectView.as_view(url='courses/')),  # Redirect root URL to /courses/
]