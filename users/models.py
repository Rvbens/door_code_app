from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.utils import timezone

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default="default.jpg",upload_to="profile_pics")

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class CustomUser(User):
    phone = models.CharField('Teléfono', max_length=20)
    phone.help_text = "Teléfono con el que nos contactaste, para confirmar su identidad a la hora de activar la cuenta."

#test feature
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.dispatch import receiver

class AuditEntry(models.Model):
    action = models.CharField(max_length=64)
    ip = models.GenericIPAddressField(null=True)
    username = models.CharField(max_length=256, null=True)
    date = models.DateTimeField(null=True, blank=True)

    def __unicode__(self):
        return '{0} - {1} - {2}'.format(self.action, self.username, self.ip)

    def __str__(self):
        return '{0} - {1} - {2}'.format(self.action, self.username, self.ip)


@receiver(user_logged_in)
def user_logged_in_callback(sender, request, user, **kwargs):  
    ip = request.META.get('REMOTE_ADDR')
    date = timezone.now()
    AuditEntry.objects.create(action='user_logged_in', ip=ip, username=user.username,date=date)


@receiver(user_logged_out)
def user_logged_out_callback(sender, request, user, **kwargs):  
    ip = request.META.get('REMOTE_ADDR')
    date = timezone.now()
    AuditEntry.objects.create(action='user_logged_out', ip=ip, username=user.username,date=date)


@receiver(user_login_failed)
def user_login_failed_callback(sender, credentials, **kwargs):
    date = timezone.now()
    AuditEntry.objects.create(action='user_login_failed', username=credentials.get('username', None),date=date)