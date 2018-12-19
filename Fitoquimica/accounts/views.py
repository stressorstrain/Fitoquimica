from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import TemplateView, FormView
from django import  forms
from accounts.validators import validation
import magic, tempfile
import accounts.validators
from django.urls import reverse
from .models import UserProjects, UserExperiments, ExpSupplies, ExpToDo, ExpEquip,ProjectDocs, ProjectMember, ProjectFacilities
from commom.models import UserProfile
from .forms import UserProjectForm, ExpForm, SupplieForm, ToDoForm, EquipForm, UploadForm, ProjectsMembersForm, ProjectFacilitiesForm


def Accounts(request):
    return redirect('home')


class Home(TemplateView):
    template_name = 'accounts/home.html'

    def get(self,request, *args, **kwargs):
        return render(request, self.template_name, {})
# TODO: criar delete views e calendários para projetos


class Projetos(TemplateView):
    template_name = 'accounts/projetos.html'
    form_class = UserProjectForm
    success_url = 'projetos'

    def get(self, request, *args, **kwargs):
        all_members = ProjectMember.objects.all().filter(user=self.user(self.request))
        all_projects = UserProjects.objects.all().filter(user=self.user(self.request))
        all_doc = ProjectDocs.objects.all().filter(user=request.user)
        return render(request, self.template_name, {
            'projetos': all_projects,
            'form': self.form_class,
            'equipe': all_members,
            'docs': all_doc,
        })

    def user(self, request):
        profile = UserProfile.objects.get(user=request.user)
        return profile


class NovoProjeto(FormView):
    template_name = 'accounts/new_geral.html'
    form_class = UserProjectForm
    success_url = 'projetos'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': self.form_class()})

    def form_valid(self, form):
        username = self.user(self.request)
        titulo = form.cleaned_data['titulo']
        description = form.cleaned_data['desription']
        state = form.cleaned_data['state']
        date_begin = form.cleaned_data['date_begin']
        date_final = form.cleaned_data['data_final']
        research_inst = form.cleaned_data['research_inst']
        facility = form.cleaned_data['facility']
        nivel = form.cleaned_data['nivel']
        students = form.cleaned_data['students']
        saving = UserProjects(
            user=username,
            titulo=titulo,
            description=description,
            current_state= state,
            date_begin=date_begin,
            date_final=date_final,
            students=students,
            research_inst=research_inst,
            facility=facility,
            nivel=nivel
        )
        saving.save()
        print(form.errors),

        all_docs = ProjectDocs.objects.all().filter(user=self.request.user)
        user_projects = UserProjects.objects.filter(user=UserProfile.objects.filter(user=self.request.user)[0])
        last = user_projects.latest('id')
        if str(titulo) == str(last):
            return  redirect(reverse('membros', kwargs={"str": last}))

        else:
            print(titulo, last)

    def user(self, request):
        profile = UserProfile.objects.get(user=request.user)
        return profile


class NovoProjetoMembros(FormView):
    template_name = 'accounts/new_membros.html'
    form_class = ProjectsMembersForm
    success_url = 'projetos'

    def get(self, request, *args, **kwargs):
        #prev = self.request.META.get('HTTP_REFERER')

        #if not prev:
            #print('none')
          #  return redirect('home')

        #if prev != 'http://127.0.0.1:8000/accounts/projetos/novo_projeto/geral':
            #print('not this')
            #return redirect('home')

        # else:
         return render(request, self.template_name, {'form': self.form_class()})

    def form_valid(self, form):
        project = UserProjects.objects.filter(titulo=self.kwargs['str'])[0]
        print(project)
        name = form.cleaned_data['name']
        coordinator = form.cleaned_data['coordinator']
        saving =  ProjectMember(user=self.user(self.request), project=project, name=name, coordinator=coordinator)
        saving.save()
        current_local = UserProjects.objects.filter(user=UserProfile.objects.filter(user=self.request.user)[0])
        last = current_local.latest('id')
        if str(project) == str(last):
            return  redirect(reverse('locais', kwargs={"str": last}))

    def user(self, request):
        profile = UserProfile.objects.get(user=request.user)
        return profile


class NovoProjetoLocais(FormView):
    template_name = 'accounts/new_facilities.html'
    form_class = ProjectFacilitiesForm
    success_url = 'projetos'

    def get(self, request, *args, **kwargs):
       # prev = self.request.META.get('HTTP_REFERER')

        #if not prev:
            #print('none')
           # return redirect('home')

        # if prev != 'http://127.0.0.1:8000/accounts/projetos/novo_projeto/geral':
            # print('not this')
            # return redirect('home')

        #else:
          return render(request, self.template_name, {'form': self.form_class()})

    def form_valid(self, form):
        project = UserProjects.objects.filter(titulo=self.kwargs['str'])[0]
        print(project)
        facility=form.cleaned_data['facility2']
        saving =  ProjectFacilities(project=project, facility2=facility)
        saving.save()
        return redirect('projetos')


class DeletarProjeto(TemplateView):
    template_name = 'accounts/projeto_delete.html'
    success_url = 'projetos'

    def get(self, request, *args, **kwargs):
        all_projects = UserProjects.objects.all().filter(user=self.user(self.request))
        for_delete=all_projects.get(pk=kwargs['pk'])
        for_delete.delete()
        return render(request, self.template_name, {})

    def user(self, request):
        profile = UserProfile.objects.get(user=request.user)
        return profile


class UploadDoc(FormView):
    template_name = 'accounts/upload_doc.html'
    success_url = 'projetos'

    def post(self,  request, *args, **kwargs):

        form = UploadForm(request.user, request.POST, request.FILES)
        mime = magic.Magic(mime=True)

        if form.is_valid():
            project = form.cleaned_data['project']
            tipo = form.cleaned_data['type']
            mime = mime.from_buffer(request.FILES['file'].read())
            validated = validation(mime, int(tipo))
            if validated:

                protocol = ProjectDocs(
                    user=self.request.user,
                    project=project,
                    type=tipo,
                    file=request.FILES['file']
                )
                protocol.save()
                return redirect('projetos')
            else:
                raise forms.ValidationError("Tipo de arquivo diferente do declarado")
        else:
            print("invalid")
            print(form.errors)

    def get(self, request, *args, **kwargs):
        form = UploadForm( request.user)
        user_profile = UserProfile.objects.all().filter(user=request.user)[0]
        all_projects = UserProjects.objects.all().filter(user=self.user(self.request))
        all_docs = ProjectDocs.objects.all().filter(user=request.user)

        return render(request, self.template_name, {'form':form, 'all_projects':all_projects, 'all_docs': all_docs})

    def user(self, request):
        profile = UserProfile.objects.get(user=request.user)
        return profile


class UserExperiment(FormView):
    template_name = 'accounts/experimentos.html'
    form_class = ExpForm
    success_url = 'planejamento'

    def get(self, request, *args, **kwargs):
        all_experiments = UserExperiments.objects.all().filter(user=self.user(self.request))
        return render(request, self.template_name, {'exps': all_experiments, 'form': self.form_class})

    def form_valid(self, form):
        print("aloha")
        username = self.user(self.request)
        name = form.cleaned_data['name']
        saving = UserExperiments(user=username, name=name)
        saving.save()
        return super().form_valid(form)

    def user(self, request):
        profile = UserProfile.objects.get(user=request.user)
        return profile


class Experimento(TemplateView):
    template_name = 'cromatografia/cromatografia.html'

    def get(self, request, *args, **kwargs):
        experiments = UserExperiments.objects.all().get(name=kwargs['str'])
        all_supplies = ExpSupplies.objects.all()
        all_todo = ExpToDo.objects.all()
        all_equip = ExpEquip.objects.all()
        return render(request, self.template_name, {
            'exps': experiments,
            'supplies': all_supplies,
            'todo': all_todo,
            'equips': all_equip}
                      )


class Materiais(FormView):
    template_name = 'accounts/materiais.html'
    form_class = SupplieForm

    def get_success_url(self,  *args,  **kwargs):
        return redirect('/accounts/planejamento/'+self.request.user.username+'/'+args[0])

    def get(self, request, *args, **kwargs):
        experiments = UserExperiments.objects.all().get(name=kwargs['str'])
        all_supplies = ExpSupplies.objects.all()
        return render(request, self.template_name, {
            'exps': experiments,
            'supplies': all_supplies,
            'form': self.form_class
        }
                      )

    def form_valid(self, form, *args, **kwargs):
        exp_name = form.cleaned_data['exp_name']
        exp = self.exp_get(exp_name)
        supplie_name = form.cleaned_data['supplie_name']
        supplie_amount = form.cleaned_data['supplie_amount']
        supplie_measurement = form.cleaned_data['supplie_measurement']
        disponibildiade = form.cleaned_data['disponibilidade']
        saving = ExpSupplies(
            exp=exp,
            exp_name=exp_name,
            supplie_name=supplie_name,
            supplie_amount=supplie_amount,
            supplie_measurement=supplie_measurement,
            disponibilidade=disponibildiade
        )
        saving.save()
        return self.get_success_url(exp_name)

    def exp_get(self, name):
        all_exp = UserExperiments.objects.get(name=name)
        return all_exp

    def form_invalid(self, form):
        print(form.errors)
        print('invalido')

    def user(self, request):
        profile = UserProfile.objects.get(user=request.user)
        return profile


class ToDo(FormView):
    template_name = 'accounts/todo.html'
    form_class = ToDoForm

    def get_success_url(self,  *args,  **kwargs):
        return redirect('/accounts/planejamento/'+self.request.user.username+'/'+args[0])

    def get(self, request, *args, **kwargs):
        experiments = UserExperiments.objects.all().get(name=kwargs['str'])
        all_todo = ExpToDo.objects.all()
        return render(request, self.template_name, {
            'exps': experiments,
            'todo': all_todo,
            'form': self.form_class
        }
                      )

    def form_valid(self, form, *args, **kwargs):
        exp_name = form.cleaned_data['exp_name']
        exp = self.exp_get(exp_name)
        note = form.cleaned_data['note']
        saving = ExpToDo(exp=exp, exp_name=exp_name,  note=note)
        saving.save()
        return self.get_success_url(exp_name)

    def exp_get(self, name):
        all_exp = UserExperiments.objects.get(name=name)
        return all_exp

    def form_invalid(self, form):
        print(form.errors)
        print('invalido')

    def user(self, request):
        profile = UserProfile.objects.get(user=request.user)
        return profile


class Equip(FormView):
    template_name = 'accounts/equip.html'
    form_class = EquipForm

    def get_success_url(self,  *args,  **kwargs):
        return redirect('/accounts/planejamento/'+self.request.user.username+'/'+args[0])

    def get(self, request, *args, **kwargs):
        experiments = UserExperiments.objects.all().get(name=kwargs['str'])
        all_equip = ExpEquip.objects.all()
        return render(request, self.template_name, {
            'exps': experiments,
            'equips': all_equip,
            'form': self.form_class
                                                    }
                      )

    def form_valid(self, form, *args, **kwargs):
        exp_name = form.cleaned_data['exp_name']
        exp = self.exp_get(exp_name)
        equipamento = form.cleaned_data['equip']
        location = form.cleaned_data['location']
        saving = ExpEquip(exp=exp, exp_name=exp_name, equip=equipamento, location=location)
        saving.save()
        return self.get_success_url(exp_name)

    def exp_get(self, name):
        all_exp = UserExperiments.objects.get(name=name)
        return all_exp

    def form_invalid(self, form):
        print(form.errors)
        print('invalido')

    def user(self, request):
        profile = UserProfile.objects.get(user=request.user)
        return profile

