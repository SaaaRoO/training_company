from django.test import TestCase
from django.urls import reverse
from courses.models import Course

class CourseViewTest(TestCase):
    def test_course_list_view(self):
        response = self.client.get(reverse('course-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Courses")

    def test_course_create_view(self):
        response = self.client.post(reverse('course-create'), {
            'title': 'Advanced Python',
            'description': 'Learn advanced Python',
            'duration': 20,
            'price': 199.99,
            'trainers': [self.trainer.id]  # Ensure this is a list of IDs
        })
        
        # Debugging: Print the response content if the status code is not 302
        if response.status_code != 302:
            print(response.content.decode())  # Print the HTML response for debugging
        
        self.assertEqual(response.status_code, 302)  # Redirect after creation
        self.assertTrue(Course.objects.filter(title='Advanced Python').exists())