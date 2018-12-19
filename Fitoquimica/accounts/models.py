from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from commom.models import UserProfile
from . import accoutns_choices as choices
from django.dispatch import receiver
from django.db.models.signals import post_delete
import datetime
import os
from datetime import date


def user_directory_path(instance, filename):
    users = User.objects.all()
    ins = instance.search()
    print(ins)
    for user in users:
        if user == instance.user:
            if ins == 'docs':
                return 'accounts/user_{0}/{1}/{2}'.format(instance.user.id, ins, filename)


class LastSeen(models.Model):
    user = models.ForeignKey(User, default=2, on_delete=models.CASCADE)
    last_seen = models.DateTimeField(auto_now=False, auto_now_add=False, default=timezone.now)

    def search(self):
        return 'lastseen'

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = "Visitas"


class UserProjects(models.Model):
    user = models.ForeignKey(UserProfile, default='guibax', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200, default="Projeto")
    description = models.CharField(max_length=2000, default='descrição')
    current_state = models.PositiveSmallIntegerField(choices=choices.PROJ_STATE, default=2)
    date_begin = models.DateField( blank=True, null=True)
    date_final =  models.DateField(blank=True, null=True)
    research_inst  = models.CharField(max_length=30, blank=False, null=False, default='Instituição de Pesquisa')
    facility = models.CharField(max_length=30, blank=False, null=False, default='Departamento')
    nivel = models.PositiveSmallIntegerField(choices=choices.NIVEL_CHOICES)
    students = models.PositiveSmallIntegerField(default=0)

    def search(self):
        return 'projects'

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name_plural = "Projetos"


class ProjectMember(models.Model):
    user = models.ForeignKey(UserProfile,default='guibax', on_delete=models.CASCADE)
    project = models.ForeignKey(UserProjects, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, blank=False, null=False)
    coordinator = models.PositiveSmallIntegerField(choices=choices.COORDENADOR)

    def search(self):
        return 'projects'

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Membros de Projetos"


class ProjectFacilities(models.Model):
    project = models.ForeignKey(UserProjects, on_delete=models.CASCADE)
    facility2 = models.CharField(max_length=30, blank=False, null=False)


class ProjectDocs(models.Model):
    user = models.ForeignKey(User, default=2, on_delete=models.CASCADE)
    project = models.ForeignKey(UserProjects, default=None, on_delete=models.CASCADE)
    type = models.PositiveSmallIntegerField(choices=choices.DOC_TYPES, default=1)
    file = models.FileField(upload_to=user_directory_path)

    def search(self):
        return 'docs'

    def filename(self):
        return os.path.basename(self.file.name).split('/')[-1]

    def __str__(self):
        return self.filename()

    class Meta:
        verbose_name_plural = 'Documentos'


class UserExperiments(models.Model):
    user = models.ForeignKey(UserProfile, default=None, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default='Experimento')

    def search(self):
        return 'experiments'

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = "Experimentos"


class ExpSupplies(models.Model):
    exp = models.ForeignKey(UserExperiments, on_delete=models.CASCADE)
    exp_name = models.CharField(max_length=50, default='HS-SPME')
    supplie_name = models.CharField(max_length=50, default="recurso")
    supplie_amount = models.PositiveIntegerField(default=1)
    supplie_measurement = models.CharField(max_length=10, default='X')
    disponibilidade = models.PositiveSmallIntegerField(choices=choices.DISP_CHOICES, default=2)

    def search(self):
        return'supplies'

    def __str__(self):
        return self.supplie_name

    class Meta:
        verbose_name_plural = 'Materiais'


class ExpToDo(models.Model):
    exp = models.ForeignKey(UserExperiments, on_delete=models.CASCADE)
    exp_name = models.CharField(max_length=50, default='HS-SPME')
    note = models.CharField(max_length=300, default='A Fazer')

    def search(self):
        return'todo'

    def __str__(self):
        return self.note

    class Meta:
        verbose_name_plural = 'Afazeres'


class ExpEquip(models.Model):
    exp = models.ForeignKey(UserExperiments, on_delete=models.CASCADE)
    exp_name = models.CharField(max_length=50, default='HS-SPME')
    equip = models.CharField(max_length=300, default='GC/MS')
    location = models.CharField(max_length=20, default='Fitoquímica')

    def search(self):
        return'equipamentos'

    def __str__(self):
        return self.equip

    class Meta:
        verbose_name_plural = 'Equipamentos'
