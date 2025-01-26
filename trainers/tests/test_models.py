from django.test import TestCase
from trainers.models import Trainer

class TrainerModelTest(TestCase):
    def test_trainer_creation(self):
        trainer = Trainer.objects.create(name="Sarah Mahmoud", email="sasoky@example.com", phone="0987654321", expertise="Django")
        self.assertEqual(trainer.name, "Jane Doe")
        self.assertEqual(trainer.expertise, "Django")