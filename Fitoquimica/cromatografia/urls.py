from django.urls import path, include
from .views import GasControl, ReservaGC, IRLK

urlpatterns = [
    path('reserva/', ReservaGC.as_view(), name='reservas'),
    path('irlk/', IRLK.as_view(), name='irlk'),
    path('control/', GasControl.as_view(), name='gas_control')

]