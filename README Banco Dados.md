categorias
    id
    nome
clientes
    id
    nome
    cpf
    endereços
        id
        unidade federativa
        cidade
        bairro
        cep
        logradouro
        numero
        complemento
    contatos
        id
        tipo
        valor
empresas
    id
    nome
    razão social
    inscrição estadual
    cnpj

produtos
    id
    nome
    categoria
    preco

venda
    data abertura
    status (1 Em Andamento, 2 Finalizada, 3 Cancelada)
    data fechamento
    valor
    cliente
    vendas_produtos
        id
        id_venda
        id_produto
        quantidade
