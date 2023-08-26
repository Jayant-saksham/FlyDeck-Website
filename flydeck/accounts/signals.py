from django.dispatch import receiver
from .models import StudentProfile, User
from django.db.models.signals import post_save


@receiver(post_save, sender=User)
def create_student_profile(sender, instance, created, **kwargs):
    if created:
        StudentProfile.objects.create(user=instance)
