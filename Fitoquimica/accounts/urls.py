from django.urls import path, include, re_path
import accounts.views as vw
from commom import urls
import urllib.parse



urlpatterns = [
    path('', vw.Accounts, name='accounts'),
    path('home', vw.Home.as_view(), name='home'),
    path('projetos', vw.Projetos.as_view(), name='projetos'),
    path('projetos/novo_projeto/geral', vw.NovoProjeto.as_view(), name='new_project'),
    path('projetos/novo_projeto/<str>/membros', vw.NovoProjetoMembros.as_view(), name='membros'),
    path('projetos/novo_projeto/<str>/local', vw.NovoProjetoLocais.as_view(), name='locais'),
    path('projeto/deletar/<pk>', vw.DeletarProjeto.as_view(), name='delete_project'),
    re_path(r'^projetos/(?P<key>\w+)/(?P<str>.*\w+)/$', vw.UploadDoc.as_view(), name='up_doc'),
    path('planejamento', vw.UserExperiment.as_view(), name='experimento'),
    path('planejamento/<str:username>/<str>', vw.Experimento.as_view(), name='planejamento'),
    path('planejamento/<str:username>/<str>/materiais', vw.Materiais.as_view(), name='materiais'),
    path('planejamento/<str:username>/<str>/todo', vw.ToDo.as_view(), name='todo'),
    path('planejamento/<str:username>/<str>/equip', vw.Equip.as_view(), name='equip'),

]
