from .models import UserProfile, UserExperiments, ExpSupplies, ExpToDo, ExpEquip, ProjectDocs, UserProjects
from django import forms
from .accoutns_choices import NIVEL_CHOICES, DISP_CHOICES, DOC_TYPES, PROJ_STATE, COORDENADOR


class UserProjectForm(forms.Form):
    titulo = forms.CharField(
        label='Título do projeto:',
        max_length=200,
        required=True,
    )

    desription = forms.CharField(
        label = 'Descrição',
        max_length=2000,
        required=True,

    )

    state = forms.ChoiceField(
        label='Situação',
        choices=PROJ_STATE,
        required=True,
    )

    date_begin = forms.DateField(
        label="Data Ínicio",
        widget=forms.TextInput(
            attrs={'placeholder': 'mm-aaaa a mm-aaaa'})
    )

    data_final = forms.DateField(
        label="Data Final",
        widget=forms.TextInput(
            attrs={'placeholder': 'mm-aaaa a mm-aaaa'})
    )

    research_inst = forms.CharField(
        label='Instituição de Pesquisa',
        max_length=30,
    )

    facility = forms.CharField(
        label='Unidade/Departamento/Orgão',
        max_length=30,
    )

    nivel = forms.ChoiceField(
        choices=NIVEL_CHOICES,
        required=True,
        )

    students = forms.IntegerField(
        label='Número de Estudantes'
    )

    def  clean_titulo(self):
        titulo = self.cleaned_data['titulo']
        compare = UserProjects.objects.all().filter(titulo=titulo)
        if compare:
            raise forms.ValidationError('Um projeto com esse titulo já existe.')

    class Meta:
        model = UserProfile


class ProjectsMembersForm(forms.Form):
    name = forms.CharField(
        label = 'Nome',
        max_length=30,
        required=True,
    )
    coordinator = forms.ChoiceField(
        label='Coordernador',
        choices=COORDENADOR,
        required=True,
    )


class UploadForm(forms.Form):
    project = forms.ModelChoiceField(label='Projeto Relacionado', queryset=UserProjects.objects.none())
    file = forms.FileField(label='Arquivo'  )
    type = forms.ChoiceField(choices=DOC_TYPES, required=True, label='Extensão do arquivo')

    class Meta:
        ProjectDocs

    def __init__(self,user,  *args, **kwargs):
        super(UploadForm, self).__init__(*args, **kwargs)
        user_profile = UserProfile.objects.all().filter(user=user)[0]
        qs = UserProjects.objects.filter(user=user_profile)
        self.fields['project'].queryset = qs


class ProjectFacilitiesForm(forms.Form):
    facility2 = forms.CharField(
        label='locais de desenvolvimento',
        max_length=30,
    )


class ExpForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label='Nome do Experimento/Protocolo',
        required=True,
    )

    class Meta:
        UserExperiments


class SupplieForm(forms.Form):
    supplie_name = forms.CharField(
        max_length=50,
        label='Nome do Material/Recurso',

    )
    supplie_amount = forms.IntegerField(
        min_value=0,
        label='Quantidade Necessária',
    )

    supplie_measurement = forms.CharField(
        max_length=10,
        label='Unidade de medida da quantidade',
        widget=forms.TextInput(
            attrs={'placeholder': 'Ex: "g", "Kg", "mL", "L", "unidade"', 'style':'font-size: 70%'}    )

    )
    disponibilidade = forms.ChoiceField(
        choices=DISP_CHOICES,
        required=True,
        )
    exp_name = forms.CharField(
        label='Projeto Relacionado'
    )

    class Meta:
        model = ExpSupplies

    #def __init__(self, user, *args, **kwargs):
       # super(SupplieForm, self).__init__(*args, **kwargs)
        #self.fields['exp'] = forms.ModelChoiceField(label='Experimento relacionado',
                                                    #queryset=UserExperiments.objects.filter(user=user),
                                                  #  )


class ToDoForm(forms.Form):
    exp_name = forms.CharField(
        label='Projeto Relacionado'
    )
    note = forms.CharField(
        label='Titulo'
    )

    class Meta:
        model = ExpToDo


class EquipForm(forms.Form):
    exp_name = forms.CharField(
        label='Projeto Relacionado'
    )
    equip = forms.CharField(
        label='Nome do Equipamento'
    )
    location = forms.CharField(
        label='Laboratório/Instituição'
    )

    class Meta:
        model = ExpEquip

