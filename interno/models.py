from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome

class Estado(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    sigla = models.CharField(max_length=2, unique=True)

class Empresa(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    cnpj = models.CharField(max_length=14, unique=True)
    razao_social = models.CharField(max_length=100)
    inscricao_estadual = models.CharField(max_length=9, unique=True)
    faturamento = models.FloatField(default = 0, max_length = 8)
    colaboradores_total = models.IntegerField(default = 0)
    


class Produto(models.Model):
    nome = models.CharField(max_length = 100, unique=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to="produtos_imagem", null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"Nome: {self.nome} Categoria: {self.categoria.nome}"
    

class Cidade(models.Model):
    nome = models.CharField(max_length = 45, unique=True)
    quantidade_habitantes = models.IntegerField(default = 0)
    clima = models.CharField(max_length = 40)
    data_fundacao = models.DateField()
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"Nome: {self.nome} Estado: {self.estado.nome}"
    

class Colaborador(models.Model):
    nome = models.CharField(max_length = 30)
    cpf = models.CharField(max_length = 11, unique=True)
    data_nascimento = models.DateField()
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)


    
