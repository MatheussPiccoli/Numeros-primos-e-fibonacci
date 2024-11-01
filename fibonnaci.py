# Criar uma função em sua linguagem preferida. A função deve receber um numero N >= 0 (deve validar o input para a função),
# e retornar o valor correspondente desse número na sequência Fibonacci.
# EX. fib(0) =0; fib(1) = 1; fib(2) = 1; fib(3) = 2; fib(5) = 5; fib(6) = 8.
# 
#     --- Criar uma função recursiva que resolva Fibonacci
# 
#     --- Criar uma função linear que resolva Fibonacci

def fibonacci(n):
    lista = [0, 1, 1]
    
    for i in range(3, n+1):
        fibo = lista[i - 2] + lista[i - 1]
        lista.append(fibo)
    return lista[n]

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


