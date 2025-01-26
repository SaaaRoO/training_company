from django.test import TestCase
from django.urls import reverse, resolve
from courses.views import CourseListView, CourseCreateView

class CourseURLTest(TestCase):
    def test_course_list_url(self):
        url = reverse('course-list')
        self.assertEqual(resolve(url).func.view_class, CourseListView)

    def test_course_create_url(self):
        url = reverse('course-create')
        self.assertEqual(resolve(url).func.view_class, CourseCreateView)