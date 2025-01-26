from venv import logger
from django.shortcuts import render

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Course

class CourseListView(ListView):
    model = Course
    template_name = 'courses/course_list.html'

class CourseCreateView(CreateView):
    model = Course
    fields = ['title', 'description', 'duration', 'price', 'trainers']
    template_name = 'courses/course_form.html'
    success_url = reverse_lazy('course-list')

    def form_valid(self, form):
        logger.info("Form is valid. Saving course...")
        return super().form_valid(form)

    def form_invalid(self, form):
        logger.error("Form is invalid. Errors: %s", form.errors)
        return super().form_invalid(form)

class CourseUpdateView(UpdateView):
    model = Course
    fields = ['title', 'description', 'duration', 'price', 'trainers']
    template_name = 'courses/course_form.html'
    success_url = reverse_lazy('course-list')

class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'courses/course_confirm_delete.html'
    success_url = reverse_lazy('course-list')
