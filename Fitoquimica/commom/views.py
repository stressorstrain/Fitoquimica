from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic import TemplateView, FormView
from .models import Avisos as avisos, UserProfile, Protocolos, CategoriasProtocolos
from accounts.models import LastSeen
from .forms import AvisosForm, ProtoForm
from commom import choices
from django.contrib import messages
from datetime import datetime, timedelta


class Avisos(FormView):
    template_name = 'commom/avisos.html'
    form_class = AvisosForm
    success_url = 'avisos'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        username = self.user(self.request)
        titulo = form.cleaned_data['titulo']
        aviso = form.cleaned_data['aviso']
        data_final  = form.cleaned_data['data_final']
        saving = avisos(user=username, titulo=titulo, aviso=aviso, data_final=data_final)
        saving.save()
        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        visita = LastSeen.objects.all().filter(user=request.user)
        if visita:
            visita.delete()

        new_seen = LastSeen(user=request.user, last_seen=timezone.now())
        new_seen.save()

        all_avisos = avisos.objects.all()

        form = AvisosForm

        return render(request, self.template_name, {'avisos': all_avisos, 'form': form, })

    def user(self, request):
        profile = UserProfile.objects.get(user=request.user)
        return profile


class DeletarAviso(TemplateView):
    template_name = 'commom/aviso_deletar.html'

    def get(self, request, *args, **kwargs):
        all_avisos = avisos.objects.all()
        for_delete = all_avisos.get(pk=kwargs['pk'])

        if for_delete.user.user == request.user:
            for_delete.delete()
            return render(request, self.template_name, {})

        else:
            print(for_delete.user, request.user)

            print("heyo")
            messages.warning(request, 'O aviso só pode ser deletado pelo seu autor')
            return redirect('avisos')

    def user(self, request):
        profile = UserProfile.objects.get(user=request.user)
        return profile


class ProtocolosView(FormView):
    template_name = 'commom/protoform.html'
    form_class = ProtoForm

    def post(self,  *args, **kwargs):
        form = ProtoForm(self.request.POST, self.request.FILES)

        if form.is_valid():

            method_class = self.cat(form.cleaned_data['method_class'])
            method_name = form.cleaned_data['method_name']
            print(method_name, method_class)

            protocol = Protocolos(
                method_class=method_class,
                method_name=method_name,
                file=self.request.FILES['file']
            )
            protocol.save()
            return redirect('protocolos')
        else:
            print("invalid")
            print(form.errors)

    def get(self, request, *args, **kwargs):
        experiments = Protocolos.objects.all()
        cats = CategoriasProtocolos
        return render(request, self.template_name, {'exps': experiments, 'form': self.form_class})

    def cat(self, choice):
        print(choice)
        result = choices.string(choice)
        cats = CategoriasProtocolos.objects.get(categoria=result)
        return cats


class ProtoTemplate(TemplateView):
    template_name = 'commom/protocolos.html'

    def get(self, request, *args, **kwargs):
        prots = Protocolos.objects.all()
        cats = CategoriasProtocolos.objects.all()
        for cat in prots:
            print(cat.method_class)
        return render(request, self.template_name, {'prots': prots, 'cats':cats})


class Equipe(TemplateView):
    template_name = 'commom/calendario2.html'
# Create your views here.
