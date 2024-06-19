from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True)

class Estado(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    sigla = models.CharField(max_length=2, unique=True)

class Empresa(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    cnpj = models.CharField(max_length=14, unique=True)
    razao_social = models.CharField(max_length=100, unique=True)
    inscricao_estadual = models.CharField(max_length=9, unique=True)
    faturamento = models.FloatField(default = 0)
    colaboradores = models.IntegerField(default = 0)