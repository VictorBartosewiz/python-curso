from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="interno_home"),
    path("categoria", views.categoria_index, name="categorias"),
    path("categoria/cadastrar", views.categoria_cadastrar),
    path("categoria/apagar/<int:id>", views.categoria_apagar),
    path("categoria/editar/<int:id>", views.categoria_editar),

    path("categoria-form", views.categoria_form_index, name="categorias_form"),
    path("categoria-form/cadastrar", views.categoria_form_cadastrar),
    path("categoria-form/apagar/<int:id>", views.categoria_form_apagar),
    path("categoria-form/editar/<int:id>", views.categoria_form_editar),
    
    path("estado", views.estado_index, name="estados"),
    path("estado/cadastrar", views.estado_cadastrar),
    path("estado/apagar/<int:id>", views.estado_apagar),
    path("estado/editar/<int:id>", views.estado_editar),
    
    path("empresa", views.empresa_index, name="empresas"),
    path("empresa/cadastrar", views.empresa_cadastrar),
    path("empresa/apagar/<int:id>", views.empresa_apagar),
    path("empresa/editar/<int:id>", views.empresa_editar),

    path("produto", views.produto_index, name="produtos"),
    path("produto/cadastrar", views.produto_cadastrar),
    path("produto/apagar/<int:id>", views.produto_apagar),
    path("produto/editar/<int:id>", views.produto_editar),

    path("cidade", views.cidade_index, name="cidades"),
    path("cidade/cadastrar", views.cidade_cadastrar),
    path("cidade/apagar/<int:id>", views.cidade_apagar),
    path("cidade/editar/<int:id>", views.cidade_editar),

    path("colaborador", views.colaborador_index, name="colaboradores"),
    path("colaborador/cadastrar", views.colaborador_cadastrar),
    path("colaborador/apagar/<int:id>", views.colaborador_apagar),
    path("colaborador/editar/<int:id>", views.colaborador_editar),

]

# Criar app
# Criar o arquivo urls
# Criar os models
# Gerar as migrations (py manage.py makemigrations nome_app)
# Aplicar as migrations  (py manage.py migrate)
# Adicionar as rotas no arquivo de urls.py do novo app
# Adicionar include do novo arquivo de rotas no urls.py do setup
# Criar pasta templates
# Criar as views no arquivo de views.py
# Criar os arquivos na pasta templates