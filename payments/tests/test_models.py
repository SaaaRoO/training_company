from django.test import TestCase
from payments.models import Payment
from trainers.models import Trainer

class PaymentModelTest(TestCase):
    def test_payment_creation(self):
        trainer = Trainer.objects.create(name="Sarah Mahmoud", email="sasoky@example.com", phone="1234567890", expertise="Python")
        payment = Payment.objects.create(trainer=trainer, amount=500.00, payment_date="2023-10-01")
        self.assertEqual(payment.amount, 500.00)
        self.assertEqual(payment.trainer.name, "John Doe")