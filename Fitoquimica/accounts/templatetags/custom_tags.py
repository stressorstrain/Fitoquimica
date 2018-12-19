from django import template
from accounts.models import LastSeen
from commom.models import Avisos
from django.contrib.auth.models import User

register = template.Library()


@register.simple_tag(takes_context=True,)
def avisos_count(context, *args, **kwargs ):
    all_avisos = Avisos.objects.all()
    print(args[0])
    usuario = User.objects.all().get(username=args[0])
    visita = LastSeen.objects.all().get(user=usuario)
    noters = 0
    for aviso in all_avisos:
        note_creation = aviso.data_inicio
        last_login = visita.last_seen
        if note_creation > last_login:
            noters += 1
    print(noters)
    return str(noters)




