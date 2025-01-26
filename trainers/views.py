from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Trainer

class TrainerListView(ListView):
    model = Trainer
    template_name = 'trainers/trainer_list.html'

class TrainerCreateView(CreateView):
    model = Trainer
    fields = ['name', 'email', 'phone', 'expertise']
    template_name = 'trainers/trainer_form.html'
    success_url = reverse_lazy('trainer-list')

class TrainerUpdateView(UpdateView):
    model = Trainer
    fields = ['name', 'email', 'phone', 'expertise']
    template_name = 'trainers/trainer_form.html'
    success_url = reverse_lazy('trainer-list')

class TrainerDeleteView(DeleteView):
    model = Trainer
    template_name = 'trainers/trainer_confirm_delete.html'
    success_url = reverse_lazy('trainer-list')
