from django.db.models.signals import post_save, pre_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile, CustomUser
from django.core.mail import send_mail
from django.conf import settings

@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):
        if created:
                Profile.objects.create(user=instance)

@receiver(post_save, sender=CustomUser)
def save_profile(sender, instance, **kwargs):
        instance.profile.save()

@receiver(pre_save, sender=CustomUser, dispatch_uid='active')
def active(sender, instance, **kwargs):
        if instance.is_active and User.objects.filter(pk=instance.pk, is_active=False).exists():
                subject = 'Cuenta activada'
                mesagge = f'Su cuenta {instance.username} ha sido activada. Ya puede entrar cuando quiera'
                from_email = settings.EMAIL_HOST_USER
                send_mail(subject, mesagge, from_email, [instance.email], fail_silently=False)

