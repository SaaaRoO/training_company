from django.urls import path
from .views import PaymentListView, PaymentCreateView, PaymentUpdateView, PaymentDeleteView

urlpatterns = [
    path('', PaymentListView.as_view(), name='payment-list'),
    path('new/', PaymentCreateView.as_view(), name='payment-create'),
    path('<int:pk>/edit/', PaymentUpdateView.as_view(), name='payment-update'),
    path('<int:pk>/delete/', PaymentDeleteView.as_view(), name='payment-delete'),
]