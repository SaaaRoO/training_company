from django.test import TestCase
from django.urls import reverse
from payments.models import Payment
from trainers.models import Trainer

class PaymentViewTest(TestCase):
    def setUp(self):
        self.trainer = Trainer.objects.create(name="John Doe", email="john@example.com", phone="1234567890", expertise="Python")

    def test_payment_list_view(self):
        response = self.client.get(reverse('payment-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Payments")

    def test_payment_create_view(self):
        response = self.client.post(reverse('payment-create'), {
            'trainer': self.trainer.id,
            'amount': 500.00,
            'payment_date': '2023-10-01',
            'notes': 'Monthly payment',
        })
        self.assertEqual(response.status_code, 302)  # Redirect after creation
        self.assertTrue(Payment.objects.filter(amount=500.00).exists())