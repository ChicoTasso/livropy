from django.urls import path
from . import views
from .views import AutorListView, AutorDetailView, AutorCreateView, AutorUpdateView, AutorDeleteView, LivroListView, LivroDetailView, LivroCreateView, LivroDeleteView, LivroUpdateView

urlpatterns = [
    path('autor/', AutorListView.as_view(), name='listar-autor'),
    path('autor/<int:id>', AutorDetailView.as_view(), name='detalhar-autor'),
    path('autor/cadastrar/', AutorCreateView.as_view(), name='cadastrar-autor'),
    path('autor/atualizar/<int:id>', AutorUpdateView.as_view(), name='atualizar-autor'),
    path('autor/deletar/<int:id>', AutorDeleteView.as_view(), name='deletar-autor'),
    path('livro/', LivroListView.as_view(), name='listar-livro'),
    path('livro/<int:pk>', LivroDetailView.as_view(), name='detalhar-livro'),
    path('livro/cadastrar/', LivroCreateView.as_view(), name='cadastrar-livro'),
    path('livro/atualizar/<int:pk>', LivroUpdateView.as_view(), name='atualizar-livro'),
    path('livro/deletar/<int:pk>', LivroDeleteView.as_view(), name='deletar-livro'),
]
