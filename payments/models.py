from django.db import models

from django.db import models
from trainers.models import Trainer

class Payment(models.Model):
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Payment to {self.trainer.name} on {self.payment_date}"
