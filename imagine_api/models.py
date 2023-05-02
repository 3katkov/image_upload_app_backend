from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.contrib.postgres.fields import ArrayField
from .utils import upload_to

 
class Plan(models.Model):
    name = models.CharField(max_length=100)
    thumbnail_sizes = ArrayField(models.PositiveIntegerField(default=list))
    original_link = models.BooleanField(default=False)
    expiring_links = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return f'{self.user.username}'

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance, plan=Plan.objects.get(id=1))

post_save.connect(create_user_profile, sender=User)


class ImageModel(models.Model):
    user = models.ForeignKey(User, default="", on_delete=models.CASCADE)
    title = models.CharField(max_length=80, blank=False, null=False)
    description = models.TextField()
    image = models.ImageField(upload_to=upload_to, blank=True, null=True)
    upload_time = models.DateTimeField(auto_now_add=True, null=True) 



