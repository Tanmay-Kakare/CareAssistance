from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class UserProfile(models.Model):
    USER_ROLE_CHOICES = [
        ('caregiver', 'Caregiver'),
        ('elderly', 'Elderly'),
    ]

    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=USER_ROLE_CHOICES)
    phone = models.CharField(max_length=15, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    health_conditions = models.TextField(null=True, blank=True)  # Only for elderly users

    def __str__(self):
        return self.user.username
    

    @property
    def is_caregiver(self):
        return self.role == 'caregiver'

    @property
    def is_elderly(self):
        return self.role == 'elderly'
    


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
