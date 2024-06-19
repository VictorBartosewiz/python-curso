from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


def index(request) -> HttpResponse:
    response = HttpResponse(content="""
    <h1>Hello World</h1>
    <a href="contato">Contato</a>
    <a href="/exemplos-basicos/jogo">Jogo</a>   
    <a href="/exemplos-basicos/calculadora-form">Calculadora</a>                     
    """)
    return response


def contato(request) -> HttpResponse:
    # Obteve o arquivo contato.html e armazenou na variável template
    template = loader.get_template(template_name="contato.html")
    # Renderizar o template armazenando na variável html
    html = template.render(context={}, request=request)
    response = HttpResponse(content=html)
    return response


def jogo(request) -> HttpResponse:
    return render(request, "jogo.html")


def calculadora(request, numero1: int = 3, numero2: int = 8) -> HttpResponse:
    soma = numero1 + numero2 # gerar a soma
    contexto_dados = {
        "n1": numero1,
        "n2": numero2,
        "soma": soma
    }
    return render(request, "calculadora.html", context=contexto_dados)


def calculadora_form(request):
    if request.method == "POST":
        # Obter o query param (que está na URL)
        numero1 = int(request.POST.get("numero1"))
        numero2 = int(request.POST.get("numero2"))
        operacao = request.POST.get("operacao")

        match(operacao):
            case "somar": resultado = numero1 + numero2
            case "subtrair": resultado = numero1 - numero2
            case "multiplicar": resultado = numero1 * numero2
            case "dividir": resultado = numero1 / numero2
    else:
        resultado = None
        
    return render(request, "calculadora-form.html", context={"resultado": resultado})


def calcular(request):
    # Obter o query param (que está na URL)
    numero1 = int(request.GET.get("numero1"))
    numero2 = int(request.GET.get("numero2"))
    operacao = request.GET.get("operacao")

    match(operacao):
        case "somar": resultado = numero1 + numero2
        case "subtrair": resultado = numero1 - numero2
        case "multiplicar": resultado = numero1 * numero2
        case "dividir": resultado = numero1 / numero2
        
    return HttpResponse(f"Resultado: {resultado}")


def carro(request):
    return render(request, "carro-form.html")

def carro_cadastrar(request):
    modelo = request.POST.get("modelo")
    ano = int(request.POST.get("ano-fabricacao"))
    preco = float(request.POST.get("preco").replace(".", "").replace(",", "."))
    # 20900.29
    cor = request.POST.get("cor")

    conteudo = { 
        "modelo": modelo,
        "ano": ano,
        "preco": preco,
        "cor": cor,
    }

    return render(request, "carro.html", context=conteudo)

# Criar rota sobre com os seguintes dados no html
#   Nome (campo)
#   Sobrenome (campo)
#   Nome completo (gerar o nome completo)
#   Idade (campo)
#   Ano de Nascimento (gerar o ano nascimento)
#   Peso (campo)
#   Altura (campo)
#   Imc (gerar o imc)
#   Imagem

# py manage.py runserver
# http://127.0.0.1:8000/exemplos-basicos/home



# Criar uma tela de cadastro carro, com os seguintes campos
# modelo input text
# preço input text
# ano fabricação input datetime-
# cor select
# <form method="POST" action="....">
    # {% csrf_token %}
    
# </form>
# if (numero > 100) and (numero < 1000):
# método: POST
# modelo = request.POST.get("modelo")

# Criar uma tela para visualizar esses dados
# Criar uma tela que contém 3 campos de lados do triangulo
# Receber esses 3 lados como post (lado1, lado2, lado3)
# Verificar o tipo do triangulo e apresentar em outra tela

