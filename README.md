- Criar o env:
    ```
    py -m venv env
    ```
- Habilitar o env
    ```
    env\Scripts\activate
    ```
- Inslatar o Django
    ```
    pip install Django
    ```
- Caso já tenha o projeto criado com requirements.txt
    ```
    pip install -r .\requirements.txt
    ```
- Gerar o arquivo de requirements.txt
    ```
    pip freeze > requirements.txt
    ```
- Criar o projeto
    ```
    django-admin startproject setup .
    ```
- Acessar o help do Django
    ```
    py manage.py --help
    ```
- Criar o app
    ```
    py manage.py startapp exemplos_basicos
    ```
https://dontpad.com/franciscosensaulas/django