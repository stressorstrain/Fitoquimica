from django.urls import path, include
from .views import Avisos, ProtocolosView, Equipe, ProtoTemplate, DeletarAviso


urlpatterns = [
    path('avisos', Avisos.as_view(), name='avisos'),
    path('avisos/deletar/<pk>', DeletarAviso.as_view(), name='deletar_aviso'),
    path('protocolos', ProtoTemplate.as_view(), name='protocolos'),
    path('protocolos/novo_protocolo', ProtocolosView.as_view(), name='new_protocolo'),
    path('equipe', Equipe.as_view(), name='equipe'),
]
# Create your models here.
