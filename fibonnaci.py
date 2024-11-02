#  --- Criar uma função linear que resolva Fibonacci

# Função que resolve a sequencia de fibonacci até o número da entrada
def fibonacci(n):
    lista = [0, 1, 1]
    fibo = 0
    for i in range(3, n+1):
        fibo = lista[i - 2] + lista[i - 1]
        lista.append(fibo)
    return lista[n]

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


