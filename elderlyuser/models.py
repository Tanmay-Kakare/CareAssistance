from django.db import models
from customuser.models import UserProfile

# Create your models here.
class HealthData(models.Model):
    elderly_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    heart_rate = models.FloatField(null=True, blank=True)
    blood_pressure = models.CharField(max_length=20, null=True, blank=True)
    steps = models.IntegerField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Health data for {self.elderly_user.user.username} at {self.timestamp}"