from django.db import models
from trainers.models import Trainer

class CourseTrainer(models.Model):
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    date_assigned = models.DateField(auto_now_add=True)  # Example of an additional field

    class Meta:
        unique_together = ('course', 'trainer') 

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    duration = models.IntegerField(help_text="Duration in hours")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    trainers = models.ManyToManyField(Trainer, through='CourseTrainer', related_name='courses')  # Use the custom intermediate model
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title