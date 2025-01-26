from django.test import TestCase
from courses.models import Course
from trainers.models import Trainer

class CourseModelTest(TestCase):
    def test_course_creation(self):
        trainer = Trainer.objects.create(name="John Doe", email="john@example.com", phone="1234567890", expertise="Python")
        course = Course.objects.create(title="Python Basics", description="Learn Python", duration=10, price=99.99)
        course.trainers.add(trainer)
        self.assertEqual(course.title, "Python Basics")
        self.assertEqual(course.trainers.count(), 1)