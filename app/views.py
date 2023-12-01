from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Autor, Livro
from .forms import AutorForm, LivroForm, RegistrationForm
from django.contrib import messages
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth import  get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from typing import Any
# Create your views here.
def home (request):
    return render(request,'home.html')

class HomeTemplateView(TemplateView):
    template_name='home.html'

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        context["livros"] = Livro.objects.all()[:5]
        context["autores"] = Autor.objects.all()[:5]
        
        return context


# def home(request):
#     noticias = Noticia.objects.all()
#     return render(request, 'home.html', {"noticias": noticias})

class AutorListView(LoginRequiredMixin,ListView):
    model=Autor
    template_name='autor/listar.html'
    context_object_name='autores'
    ordering='-nome'
    paginate_by = 5

    def get_queryset(self):
        search = self.request.GET.get("q")
        
        if search:
            self.autores = Autor.objects.filter(nome__icontains=search)
        else:
            self.autores = Autor.objects.all()

        return self.autores


# def listar(request):
#     autores = Autor.objects.all().order_by('-nome')
#     return render(request, 'listar.html', {'autores':autores})

class AutorDetailView(LoginRequiredMixin,DetailView):
    model=Autor
    template_name='autor/detalhar.html'
    context_object_name='autor'
    pk_url_kwarg='id'


# def detalhar(request, id):
#     autor = Autor.objects.get(id=id)
#     return render(request, 'detalhar.html', {'autor':autor})


class AutorCreateView(LoginRequiredMixin,CreateView):
    model=Autor
    template_name='autor/cadastrar.html'
    form_class=AutorForm
    permission_required='livro.add_autor'
    

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Autor cadastrado com sucesso!")
        return reverse('listar-autor')



# def cadastrar(request):
#     if request.method == "POST":
#         form = AutorForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             messages.add_message(request, messages.SUCCESS, "Autor cadastrado com sucesso!")
#             return redirect("listar")
#     else:
#          form = AutorForm()
#          return render(request, 'cadastrar.html', {'form': form})


class AutorUpdateView(LoginRequiredMixin,UpdateView):
    model=Autor
    template_name='autor/atualizar.html'
    form_class=AutorForm
    pk_url_kwarg='id'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Autor atualizado com sucesso!")
        return reverse('listar-autor')


# def atualizar(request, id):
#     autor = Autor.objects.get(id=id)
#     form = AutorForm(instance=autor)
#     if request.method == "POST":
#         form = AutorForm(request.POST, request.FILES, instance=autor)
#         if form.is_valid():
#             form.save()
#             return redirect("atualizar", id=id)
#         else:
#             return render(request, 'atualizar.html', {'form': form})
#     else:
#          return render(request, 'atualizar.html', {'form': form})

class AutorDeleteView(LoginRequiredMixin,DeleteView):
    model=Autor
    template_name='autor/autor_confirm_delete.html'
    pk_url_kwarg='id'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Autor deletado com sucesso!")
        return reverse('listar-autor')


# def deletar(request, id):
#     autor = Autor.objects.get(id=id)
#     autor.delete()
#     return redirect('listar')


class LivroListView(LoginRequiredMixin,ListView):
    model=Livro
    template_name='livro/listar.html'
    context_object_name='livros'
    ordering='-titulo'
    paginate_by = 5


class LivroDetailView(LoginRequiredMixin,DetailView):
    model=Livro
    template_name='livro/detalhar.html'
    context_object_name='livro'


class LivroCreateView(LoginRequiredMixin,CreateView):
    model=Livro
    template_name='livro/cadastrar.html'
    form_class=LivroForm
    

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Livro cadastrada com sucesso!")
        return reverse('listar-livro')
    

class LivroUpdateView(LoginRequiredMixin,UpdateView):
    model=Livro
    template_name='livro/atualizar.html'
    form_class=LivroForm

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Livro atualizada com sucesso!")
        return reverse('listar-livro')
    

class LivroDeleteView(LoginRequiredMixin,DeleteView):
    model=Livro
    template_name='livro/livro_confirm_delete.html'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Livro deletada com sucesso!")
        return reverse('listar-livro')
    

class RegistrationView(CreateView):
    template_name = 'registration/registration.html'
    model = get_user_model()
    form_class = RegistrationForm
    
    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Cadastro realizado com sucesso!")
        return reverse('home')
   
class PerfilAutor(TemplateView):
    template_name='autor/perfil.html'
