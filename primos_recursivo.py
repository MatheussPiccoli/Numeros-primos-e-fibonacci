# A função deve receber um numero N > 1 (validar o input), e retornar todos os números primos até o número N.
# --- Criar uma função linear que resolva p


# Função que define os números primos

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

# Função para armazenar os valores primos em uma lista, de maneira recursiva

def armazena_valores(n_atual, n_limite, valores=[]):
    if n_atual >= n_limite:
        return valores
    if primos(n_atual):
        valores.append(n_atual)
    return armazena_valores(n_atual + 1, n_limite, valores)

# Validação da entrada

entrada = 0
while entrada <= 1:
    entrada = input("Digite um número inteiro N > 1: ")
    if entrada.isdigit():
        entrada = int(entrada)
        if entrada > 1:
            break
        else:
            print("O número digitado não corresponde a instrução")
    else:
       print("A entrada não é um número inteiro")

print(f"p({entrada}) = {armazena_valores(1, entrada)}")
