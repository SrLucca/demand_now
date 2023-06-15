from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.



class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)


class Profile(models.Model):

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    profile_image = models.ImageField(default='profile.png', upload_to='users', null=False, blank=True)
    def __str__(self):
        return '%s'%(self.user)


@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()