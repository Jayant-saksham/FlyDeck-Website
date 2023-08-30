from django.dispatch import receiver
from .models import StudentProfile, User
from django.db.models.signals import post_save, pre_delete


@receiver(post_save, sender=User)
def create_student_profile(sender, instance, created, **kwargs):
    if created:
        StudentProfile.objects.create(user=instance)

@receiver(pre_delete, sender=User)
def delete_student_profile(sender, instance, **kwargs):
    try:
        student_profile = instance.StudentProfile
    except StudentProfile.DoesNotExist:
        return
    
    student_profile.is_active = False
    student_profile.save()