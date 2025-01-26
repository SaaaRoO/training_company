from django.shortcuts import render

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Payment

class PaymentListView(ListView):
    model = Payment
    template_name = 'payments/payment_list.html'

class PaymentCreateView(CreateView):
    model = Payment
    fields = ['trainer', 'amount', 'payment_date', 'notes']
    template_name = 'payments/payment_form.html'
    success_url = reverse_lazy('payment-list')

class PaymentUpdateView(UpdateView):
    model = Payment
    fields = ['trainer', 'amount', 'payment_date', 'notes']
    template_name = 'payments/payment_form.html'
    success_url = reverse_lazy('payment-list')

class PaymentDeleteView(DeleteView):
    model = Payment
    template_name = 'payments/payment_confirm_delete.html'
    success_url = reverse_lazy('payment-list')
