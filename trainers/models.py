from django.db import models

from django.db import models

class Trainer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    expertise = models.CharField(max_length=200)
    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
