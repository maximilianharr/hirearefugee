from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserDetails(models.Model):
    # User Profile
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        )

    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    image = models.ImageField(upload_to='userclass/images', blank=True)
    is_refugee = models.BooleanField(null=True, default=False)

    # Ratings
    rating_val = models.FloatField(blank=True, default=0.0)
    rating_num = models.IntegerField(blank=True, default=0)

    # This is how user is displayed in Admin page
    def __str__(self):
        return 'Details of ' + self.user.username

@receiver(post_save, sender=User)
def create_userdetails(sender, instance, created, **kwargs):
    if created:
        print('create_userdetails')
        UserDetails.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_userdetails(sender, instance, **kwargs):
    print('save_userdetails')
    instance.userdetails.save()