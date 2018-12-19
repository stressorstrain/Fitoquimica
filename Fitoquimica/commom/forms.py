from .models import Avisos, UserProfile, Protocolos, CategoriasProtocolos
from django import forms
from commom import choices


class AvisosForm(forms.Form):
    titulo = forms.CharField(
        label='Título para o aviso.',
        max_length=30,
        required=True,
    )
    aviso = forms.CharField(
        label='Descrição do aviso',
        max_length=2000,
        required=True,
        widget=forms.Textarea(
            attrs={'placeholder':'Descrição do aviso', 'style': 'font-size:120%'}
        )
    )
    data_final = forms.DateField(
        label="Data Final",
        widget=forms.TextInput(
            attrs={'placeholder': 'dd-mm-aaaa'})
    )

    class Meta:
        model = Avisos


class ProtoForm(forms.Form):
    method_name = forms.CharField(
        label='Título para o protocolo.',
        max_length=30,
        required=True,
    )
    file = forms.FileField()
    method_class = forms.ChoiceField(label='Categria relacionada', choices=choices.CATEGORIA_CHOICES)

    #def __init__(self, categoria, *args, **kwargs):
        #super(ProtoForm, self).__init__(*args, **kwargs)
        #self.fields['method_class'] = forms.ModelChoiceField(
            #label='Categria relacionada',
            #queryset=categoria.objects.order_by().values_list('categoria'),
                                                   #)

    class Meta:
        model = Protocolos
