# Modelo Números primos linear

#Função que define se o número é primo

def primos(n):
    if n == 1:
        return False
    elif n != 2 and n % 2 == 0:
        return False
    else:
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
    return True

# Função responsável por armazenar os valores primos menores que a entrada em uma lista

def primos_sequencia(n):
    lista_primos = []
    for i in range(2, n + 1):
        if primos(i):
            lista_primos.append(i)
    return lista_primos

# Validação da entrada
while True:
    entrada = input("Digite um valor N > 1: ")
    if entrada.isdigit():
        entrada = int(entrada)
        if entrada > 1:
            break
        else:
            print("Número inválido")
    else:
        print("A entrada que você forneceu não é um número.")

lista_final = primos_sequencia(entrada)
print(f"p({entrada}) = {lista_final}")
