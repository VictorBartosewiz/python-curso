# Criar novo projeto
```
py manage.py startapp nome_app
```

# Adicionar o app no settings.py
Adicionar no `INSTALLED_APPS` o nome do app criado no arquivo settings.py
```
INSTALLED_APPS = [
    'django.contrib.admin',
    ...
    'nome_app',
]
```

# Criar arquivo urls.py no app que foi criado


# 
py .\manage.py makemigrations interno