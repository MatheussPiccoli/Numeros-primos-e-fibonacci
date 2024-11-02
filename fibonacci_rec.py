#     --- Criar uma função recursiva que resolva Fibonacci

# Função recursiva para fibonacci

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)

# Validação da entrada
while True:
    entrada = input("Entrada (Número inteiro >= 0): ")
    if entrada.isdigit():
        entrada = int(entrada)
        if entrada >= 0:
            break
        else:
            print("Número Inválido")
    else:
        print("Os dados do usuário não são válidos para a entrada")
        
    
resposta = fibonacci(entrada)
print(f"fib({entrada}) = {resposta}")
