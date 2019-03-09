from django.dispatch import Signal, receiver
from django.utils import timezone
from .models import RegistroActividad

home_signal = Signal(providing_args=["usuario","ip"])

@receiver(home_signal)
def home_logged(sender, usuario, ip, **kwargs):  
    fecha = timezone.now()
    RegistroActividad.objects.create(ip=ip, usuario=usuario, fecha=fecha)

