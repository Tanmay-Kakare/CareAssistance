from django.db import models
from customuser.models import UserProfile

# Create your models here.
class MedicationReminder(models.Model):
    elderly_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    medicine_name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=50)
    time = models.TimeField()

    def __str__(self):
        return f"Reminder for {self.elderly_user.user.username} to take {self.medicine_name} at {self.time}"