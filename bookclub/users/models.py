from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save #Use Django signals to create a profile when a user registers
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    favorite_genre = models.CharField(max_length=100, blank=True)   
    
    def __str__(self):
        return f"{self.user.username}'s Profile" 
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)   
        
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    
