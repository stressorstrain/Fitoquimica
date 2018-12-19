from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class GasForm(forms.Form):
    Ar_Sintético = forms.IntegerField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'volume em números'
            }
        )
    )
    Hidrogênio = forms.IntegerField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'volume em números'
            }
        )
    )
    Hélio = forms.IntegerField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'volume em números'
            }
        )
    )
    Nome_do_Verificador = forms.CharField(
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'nome e sobrenome'
            }
        )
    )
    Data_de_Verificacao = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'dd/mm/aaaa'
            }
        )
    )


