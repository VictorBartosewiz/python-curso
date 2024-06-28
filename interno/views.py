from pathlib import Path
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from interno.forms import CategoriaForm
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


# http://127.0.0.1:8000/interno/categoria-form
def categoria_form_index(request):
    # Consultar os registros da tabela de categorias (SELECT)
    categorias = models.Categoria.objects.all()
    contexto = {
        "categorias": categorias
    }
    return render(
        request, 
        "categorias_forms/index.html", 
        context=contexto,
    )


# http://127.0.0.1:8000/interno/categoria-form/cadastrar
def categoria_form_cadastrar(request):
    # Verificando se a request é do tipo POST
    if request.method == "POST":
        # construindo o form com os dados que o usuário preencheu
        form = CategoriaForm(request.POST)
        # valida se o dados preenhcidos que estão no form são válidos
        if form.is_valid():
            # Criar a categoria nesse caso
            form.save()
            # Redirecionar para a lista de categorias
            return redirect("categorias_form")
    # Caso da requisição do tipo GET
    else:
        # Criando o form vazio
        form = CategoriaForm()
    # criando o contexto passando o form
    contexto = {"form": form}
    # retornar o html do form
    return render(request, "categorias_forms/cadastrar.html", context=contexto)


def categoria_form_apagar(request, id: int):
    # Buscar a categoria que contém o id que veio na rota
    categoria = models.Categoria.objects.get(pk=id)
    # DELETE FROM categoria WHERE id = 2
    # Executar o delete na tabela de categoria filtrando por id
    categoria.delete()
    # Redireciona para a tela de listagem de categorias
    return redirect("categorias_form")


def categoria_form_editar(request, id: int):
    categoria = models.Categoria.objects.get(pk=id)
    if request.method == "POST":
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect("categorias_form")
    else:
        form = CategoriaForm(instance=categoria)
    contexto = {
        "form": form,
        "categoria": categoria,
    }
    return render(request, "categorias_forms/editar.html", contexto)
# git status
# git add .
# git commit -m "Exemplo de form.Models em categorias-form"
# git push origin main

def estado_index(request):
    estados = models.Estado.objects.all()
    contexto = {
        "estados": estados
    }
    return render(
        request,
        "estado/index.html",
        context=contexto
    )

def estado_cadastrar(request):
    if request.method == "GET":
        return render(request, "estado/cadastrar.html")
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
        return render(request, "estado/editar.html", context=contexto)
    
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
        "empresa/index.html",
        context=contexto
    )

def empresa_cadastrar(request):
    if request.method == "GET":
        return render(request, "empresa/cadastrar.html")
    nome = request.POST.get("nome").strip()
    cnpj = request.POST.get("cnpj").strip()
    razao_social = request.POST.get("razao_social").strip()
    inscricao_estadual = request.POST.get("inscricao_estadual").strip()
    faturamento = request.POST.get("faturamento").strip()
    colaboradores_total = request.POST.get("colaboradores_total").strip()
    
    empresa = models.Empresa(nome=nome, cnpj=cnpj, razao_social = razao_social, inscricao_estadual = inscricao_estadual, faturamento = faturamento, colaboradores_total = colaboradores_total)
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
        return render(request, "empresa/editar.html", context=contexto)

    empresa.nome = request.POST.get("nome").strip()
    empresa.cnpj = request.POST.get("cnpj").strip()
    empresa.razao_social = request.POST.get("razao_social").strip()
    empresa.inscricao_estadual = request.POST.get("inscricao_estadual").strip()
    empresa.faturamento = request.POST.get("faturamento").strip()
    empresa.colaboradores_total = request.POST.get("colaboradores_total").strip()
    
    empresa.save()
    return redirect("empresas")

def produto_index(request):
    produtos = models.Produto.objects.all()
    contexto = {"produtos": produtos}
    return render(request, "produtos/index.html", context=contexto)


def produto_cadastrar(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        preco = request.POST.get("preco")
        id_categoria = request.POST.get("categoria")
        descricao = request.POST.get("descricao")
        imagem = __upload_imagem(request)
        produto = models.Produto(
            nome=nome,
            preco=preco,
            descricao=descricao,
            categoria_id=id_categoria,
            imagem=imagem,
        )
        produto.save()
        return redirect("produtos")
    categorias = models.Categoria.objects.all()
    contexto = {"categorias": categorias}
    return render(request, "produtos/cadastrar.html", contexto)

def __upload_imagem(request):
    if not request.FILES:
        return None
    imagem = request.FILES.get("imagem", None)
    if not imagem:
        return None
    
    salvador = FileSystemStorage()
    caminho_arquivo = Path("produtos_imagens") / imagem.name
    nome_arquivo = salvador.save(caminho_arquivo, imagem)
    return nome_arquivo 

def produto_apagar(request, id: int):
    produto = models.Produto.objects.get(pk=id)
    produto.delete()
    return redirect("produtos")

def produto_editar(request, id: int):
    produto = models.Produto.objects.get(pk=id)

    if request.method == "POST":
        nome = request.POST.get("nome")
        preco = request.POST.get("preco")
        id_categoria = request.POST.get("categoria")
        descricao = request.POST.get("descricao")
        produto.nome = nome
        produto.preco = preco
        produto.descricao = descricao
        produto.categoria_id = id_categoria
        produto.save()
        return redirect("produtos")
    
    categorias = models.Categoria.objects.all()
    contexto = {
        "categorias": categorias,
        "produto": produto,
    }
        
    return render (request, "produtos/editar.html", contexto)


def cidade_index(request):
    cidades = models.Cidade.objects.all()
    contexto = {"cidades": cidades}
    return render(request, "cidades/index.html", context=contexto)

def cidade_apagar(request, id: int):
    cidade = models.Cidade.objects.get(pk=id)
    cidade.delete()
    return redirect("cidades")


def cidade_cadastrar(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        quantidade_habitantes = request.POST.get("quantidade_habitantes")
        clima = request.POST.get("clima")
        data_fundacao = request.POST.get("data_fundacao")
        id_estado = request.POST.get("estado")
        cidade = models.Cidade(
            nome=nome,
            quantidade_habitantes=quantidade_habitantes,
            clima=clima,
            data_fundacao=data_fundacao,
            estado_id=id_estado
        )
        cidade.save()
        return redirect("cidades")
    estados = models.Estado.objects.all()
    contexto = {"estados": estados}
    return render(request, "cidades/cadastrar.html", contexto)


def cidade_editar(request, id: int):
    cidade = models.Cidade.objects.get(pk=id)
    
    if request.method == "POST":
        nome = request.POST.get("nome")
        quantidade_habitantes = request.POST.get("quantidade_habitantes")
        clima = request.POST.get("clima")
        data_fundacao = request.POST.get("data_fundacao")
        id_estado = request.POST.get("estado")
        cidade.nome = nome
        cidade.quantidade_habitantes = quantidade_habitantes
        cidade.clima = clima
        cidade.data_fundacao = data_fundacao
        cidade.estado_id = id_estado
        cidade.save()
        return redirect("cidades")
    
    estados = models.Estado.objects.all()
    contexto = {
        "estados": estados,
        "cidade": cidade,
    }
    
    return render(request, "cidades/editar.html", contexto)


def colaborador_index(request):
    colaboradores = models.Colaborador.objects.all()
    contexto = {"colaboradores": colaboradores}
    return render(request, "colaborador/index.html", context=contexto)


def colaborador_apagar(request, id: int):
    colaborador = models.Colaborador.objects.get(pk=id)
    colaborador.delete()
    return redirect("colaboradores")


def colaborador_cadastrar(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        cpf = request.POST.get("cpf")
        data_nascimento = request.POST.get("data_nascimento")
        id_empresa= request.POST.get("empresa")
        colaborador = models.Colaborador(
            nome=nome,
            cpf=cpf,
            data_nascimento=data_nascimento,
            empresa_id=id_empresa,
        )
        colaborador.save()
        return redirect("colaboradores")
    empresas = models.Empresa.objects.all()
    contexto = {"empresas": empresas}
    return render(request, "colaborador/cadastrar.html", contexto)

def colaborador_editar(request, id: int):
    colaborador = models.Colaborador.objects.get(pk=id)
    if request.method == "POST":
        nome = request.POST.get("nome")
        cpf = request.POST.get("cpf")
        data_nascimento = request.POST.get("data_nascimento")
        id_empresa= request.POST.get("empresa")
        colaborador.nome = nome
        colaborador.cpf = cpf
        colaborador.data_nascimento = data_nascimento
        colaborador.empresa.id = id_empresa
        colaborador.save()
        return redirect("colaboradores")

    empresas = models.Empresa.objects.all()
    contexto = {
        "empresas": empresas,
        "colaborador": colaborador,
    }

    return render(request, "colaborador/editar.html", contexto)


        