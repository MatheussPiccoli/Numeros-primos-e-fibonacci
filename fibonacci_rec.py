# Criar uma função em sua linguagem preferida. A função deve receber um numero N >= 0 (deve validar o input para a função),
# e retornar o valor correspondente desse número na sequência Fibonacci.
# EX. fib(0) =0; fib(1) = 1; fib(2) = 1; fib(3) = 2; fib(5) = 5; fib(6) = 8.
# 
#     --- Criar uma função recursiva que resolva Fibonacci
# 
#     --- Criar uma função linear que resolva Fibonacci
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)

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
