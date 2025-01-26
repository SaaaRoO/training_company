from django.test import TestCase
from trainers.models import Trainer
from trainers.forms import TrainerForm

class TrainerFormTest(TestCase):
    def test_valid_form(self):
        form_data = {
            'name': 'Sarah Mahmoud',
            'email': 'john@example.com',
            'phone': '+1234567890',
            'expertise': 'Python'
        }
        form = TrainerForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_email(self):
        form_data = {
            'name': 'Sarah Mahmoud',
            'email': 'invalid-email',
            'phone': '+0987654321',
            'expertise': 'Django'
        }
        form = TrainerForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)