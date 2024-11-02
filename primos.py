#  2 - Números primos
#      -- Criar uma função em sua linguagem preferida. A função deve receber um numero N > 1 (validar o input),
# e retornar todos os números primos até o número N. EX. p(2) = [2]; p(3) = [2, 3]; p(10) = [2, 3, 5, 7];

def primos(n):
    lista_primos = []
    for i in range(1, n+1):
        primo = True
        for j in range(2, i):
            if i % j == 0:
                primo = False
        if primo == True:
            lista_primos.append(i)    
    return lista_primos
        
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

lista_final = primos(entrada)
print(f"p({entrada}) = {lista_final}")

    
            
