from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Gas
from .forms import GasForm
from . import gas


class GasControl(TemplateView):
    template_name = 'cromatografia/gas_control.html'
    model = Gas
    # TODO: CRIAR CALENDÁRIOS

    def get(self, request, *args, **kwargs):
        form = GasForm()
        gases = Gas.objects.order_by('created_at').reverse()[:1]
        args = {'gasform': form, 'gases': gases}
        return render(request, self.template_name, args)

    def post(self, request, *args, **kwargs):
        form = GasForm(request.POST)
        gases = Gas.objects.order_by('created_at').reverse()[:1]

        if form.is_valid():
            ars = form.cleaned_data['Ar_Sintético']
            ars_p = self.porcentagem(ars, 'ars')
            h2 = form.cleaned_data['Hidrogênio']
            h2_p = self.porcentagem(h2, 'h2')
            he = form.cleaned_data['Hélio']
            he_p = self.porcentagem(he, 'he')
            ver_name = form.cleaned_data['Nome_do_Verificador']
            ver_date = form.cleaned_data['Data_de_Verificacao']
            new_data = (str(ver_date)+"\t"+str(ars)+"\t"+str(h2)+"\t"+str(he))
            if gas.start(new_data):
                data = Gas(ars=ars, h2=h2, he=he, ars_p=ars_p, h2_p=h2_p, he_p=he_p, ver_name=ver_name, ver_date=ver_date)
                data.save()
                form = GasForm()
            return redirect('cromatografia')

        args = {'gasform': form, 'gases': gases}
        return render(request, self.template_name, args)

    def porcentagem(self, cvol, ind):
        ars = ['Ar Sintético', 'Ar Sintetico', 'ar sintético', 'ar sintetico', 'ars']
        h2 = ['Hidrogênio', 'Hidrogenio', 'hidrogenio', 'hidrogênio', 'h2']
        he = ['Hélio', 'Helio', 'hélio', 'helio', 'he']
        if ind in ars:
            mvol = 18000
            return (cvol * 100) / mvol
        elif ind in h2:
            mvol = 16000
            return (cvol * 100) / mvol
        elif ind in he:
            mvol = 150
            return (cvol * 100) / mvol


class ReservaGC(FormView):
    print('hi')
    template_name = 'cromatografia/crom_reservas.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})


class IRLK(FormView):
    print('hi')
    template_name = 'cromatografia/crom_reservas.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})

