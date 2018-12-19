from django.db import models
from django.contrib.auth.models import User
import datetime
import os


def user_directory_path(instance, filename):
    users = User.objects.all()
    ins = instance.search()
    print(ins)
    for user in users:
        if user == instance.user:
            if ins == 'avatar':
                return 'accounts/user_{0}/{1}/{2}'.format(instance.user.id, ins, filename)

        elif ins == 'files':
                print("oks")
                return 'accounts/user_{0}/{1}/{2}'.format(instance.user.id, ins, filename)


def protocol_directory_path(instance, categoria):
    categorias = CategoriasProtocolos.objects.all().filter


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    lates = models.CharField(max_length=300, blank=False, null=False, default='http://lattes.cnpq.br/')
   #  avatar = models.ImageField(upload_to=user_directory_path, blank=True, )

    def __str__(self):
        return self.user.username

    def search(self):
        return 'avatar'


class Avisos(models.Model):
    user = models.ForeignKey(UserProfile, default=None, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=30, default='Aviso')
    aviso = models.CharField(max_length=2000, default="AVISO", blank=False, null=False)
    data_inicio = models.DateTimeField(auto_now_add=True)
    data_final = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name_plural = "Avisos"


class CategoriasProtocolos(models.Model):
    categoria = models.CharField(max_length=50, default='Extração')

    def __str__(self):
        return self.categoria

    def search(self):
        return 'categorias'

    class Meta:
        verbose_name_plural = "Categorias"


class Protocolos(models.Model):
    method_name = models.CharField(max_length=20, default='Método')
    method_class = models.ForeignKey(CategoriasProtocolos, default=None, on_delete=models.CASCADE, blank=True, null=True)
    file = models.FileField(upload_to='protocolos')

    def search(self):
        return 'protocolos'

    def __str__(self):
        return self.method_name

    class Meta:
        verbose_name_plural = "Protocolos"