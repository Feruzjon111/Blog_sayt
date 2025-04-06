from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Profile
from django.core.mail import send_mail
from django.conf import settings
import logging

# Loggerni sozlash
logger = logging.getLogger(__name__)

# User yaratishda Profile yaratish
@receiver(post_save, sender=User)
def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name,
        )
        # Email yuborish
        subject = 'Welcome to DevSearch'
        message = 'We are glad you are here!'
        try:
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [profile.email],
                fail_silently=False,
            )
        except Exception as e:
            logger.error(f"Error sending email to {profile.email}: {e}")

# Profile yangilanishida Userni yangilash
@receiver(post_save, sender=Profile)
def updateUser(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user
    if not created:  # created == False
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        try:
            user.save()
        except Exception as e:
            logger.error(f"Error updating user {user.username}: {e}")

# Profile o‘chirilib ketganda Userni o‘chirish
@receiver(post_delete, sender=Profile)
def deleteUser(sender, instance, **kwargs):
    try:
        user = instance.user
        user.delete()
    except Exception as e:
        logger.error(f"Error deleting user: {e}")
