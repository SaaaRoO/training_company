from django.test import TestCase
from django.urls import reverse
from trainers.models import Trainer

class TrainerViewTest(TestCase):
    def test_trainer_list_view(self):
        response = self.client.get(reverse('trainer-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Trainers")

    def test_trainer_create_view(self):
        response = self.client.post(reverse('trainer-create'), {
            'name': 'Sarah Mahmoud',
            'email': 'sasoky@example.com',
            'phone': '0987654321',
            'expertise': 'Django',
        })
        self.assertEqual(response.status_code, 302)  # Redirect after creation
        self.assertTrue(Trainer.objects.filter(name="Jane Doe").exists())