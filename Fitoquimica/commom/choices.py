import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Fitoquimica.settings")
django.setup()
from commom.models import CategoriasProtocolos

alls = CategoriasProtocolos.objects.values_list('categoria')
start = 0
tuples = ()


def cat(tuples, start):
    for i in alls:
        nw_tp = (start, )
        nw_tp = nw_tp + (i[0], )
        tuples = tuples+(nw_tp,)
        start = start + 1
    return(tuples)


def string(num):
    choices = cat(tuples, start)
    for ch in choices:
        if num == str(ch[0]):
            choice = ch[1]
            return choice


CATEGORIA_CHOICES = cat(tuples, start)
