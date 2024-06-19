
                                    =valor padrão
def somar(numero1: int, numero2: int=2) -> int:
    soma = numero1 + numero2
    return soma


print(somar(1, 3))
print(somar(1))