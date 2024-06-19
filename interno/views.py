from django.shortcuts import render, redirect
from . import models


def home(request):
    return render(request, "home.html")


def categoria_index(request):
    # Consultar os registros da tabela de categorias (SELECT)
    categorias = models.Categoria.objects.all()
    contexto = {
        "categorias": categorias
    }
    return render(
        request, 
        "categorias/index.html", 
        context=contexto,
    )


def categoria_cadastrar(request):
    if request.method == "GET":
        return render(request, "categorias/cadastrar.html")
    # Obtendo os dados que o usuário preencheu nos campos
    nome = request.POST.get("nome").strip()
    # instanciando um objeto da classe Categoria
    # preenchendo os atributos (nome)
    categoria = models.Categoria(nome=nome)
    # Executando a rotina de criar o registro na tabela de Categorias (INSERT INTO)
    categoria.save()
    # Redirecionar para a lista de categorias (categoria_index)
    return redirect("categorias")


# /categoria/apagar/<id>
def categoria_apagar(request, id: int):
    # Buscar a categoria que contém o id que veio na rota
    categoria = models.Categoria.objects.get(pk=id)
    # DELETE FROM categoria WHERE id = 2
    # Executar o delete na tabela de categoria filtrando por id
    categoria.delete()
    # Redireciona para a tela de listagem de categorias
    return redirect("categorias")

# /categoria/editar/<id>
def categoria_editar(request, id: int):
    categoria = models.Categoria.objects.get(pk=id)
    if request.method == "GET":
        contexto = { "categoria": categoria}
        return render(request, "categorias/editar.html", context=contexto)

    categoria.nome = request.POST.get("nome").strip()
    categoria.save()
    return redirect("categorias")

def estado_index(request):
    estados = models.Estado.objects.all()
    contexto = {
        "estados": estados
    }
    return render(
        request,
        "estados/index.html",
        context=contexto
    )

def estado_cadastrar(request):
    if request.method == "GET":
        return render(request, "estados/cadastrar.html")
    nome = request.POST.get("nome").strip()
    sigla = request.POST.get("sigla")

    estado = models.Estado(nome=nome, sigla=sigla)
    estado.save()
    return redirect("estados")

def estado_apagar(request, id: int):
    estado = models.Estado.objects.get(pk=id)
    estado.delete()
    return redirect("estados")

def estado_editar(request, id:int):
    estado = models.Estado.objects.get(pk=id)
    if request.method == "GET":
        contexto = {"estado": estado}
        return render(request, "estados/editar.html", context=contexto)
    
    estado.nome = request.POST.get("nome").strip()
    estado.sigla = request.POST.get("sigla").strip()
    estado.save()
    return redirect("estados")

def empresa_index(request):
    empresas = models.Empresa.objects.all()
    contexto = {
        "empresas": empresas
    }
    return render(
        request,
        "empresas/index.html",
        context=contexto
    )

def empresa_cadastrar(request):
    if request.method == "GET":
        return render(request, "empresas/cadastrar.html")
    nome = request.POST.get("nome").strip()
    cnpj = request.POST.get("cnpj").strip()
    razao_social = request.POST.get("razao_social").strip()
    inscricao_estadual = request.POST.get("inscricao_estadual").strip()
    faturamento = request.POST.get("faturamento").strip()
    colaboradores = request.POST.get("colaboradores").strip()
    
    empresa = models.Empresa(nome=nome, cnpj=cnpj, razao_social = razao_social, inscricao_estadual = inscricao_estadual, faturamento = faturamento, colaboradores = colaboradores)
    empresa.save()
    return redirect("empresas")

def empresa_apagar(request, id: int):
    empresa = models.Empresa.objects.get(pk=id)
    empresa.delete()
    return redirect("empresas")

def empresa_editar(request, id:int):
    empresa = models.Empresa.objects.get(pk=id)
    if request.method == "GET":
        contexto = { "empresa": empresa}
        return render(request, "empresas/editar.html", context=contexto)

    empresa.nome = request.POST.get("nome").strip()
    empresa.cnpj = request.POST.get("cnpj").strip()
    empresa.razao_social = request.POST.get("razao_social").strip()
    empresa.inscricao_estadual = request.POST.get("inscricao_estadual").strip()
    empresa.faturamento = request.POST.get("faturamento").strip()
    empresa.colaboradores = request.POST.get("colaboradores").strip()
    
    empresa.save()
    return redirect("empresas")