# Exercício 1 - while
'''
resposta = 1

while resposta != 0:
    print("\nOlá Mundo!\n")
    print("Quer ver a mensagem novamente?")
    resposta = int(input("Digite 1 para 'sim' e 0 para 'não': "))

print("FIM")
'''


# Exercício 2 - for
'''
for n in range(0, 101, 10):
    print(n)
'''


# Exercício 3
'''
soma = 0
n = int(input("Digite um número 'n' para calcular a soma de todos os números até 'n': "))

while n <= 0:
    print("Somente valores maiores que zero")
    n = int(input("Digite um número 'n' para calcular a soma de todos os números até 'n': "))

for num in range(1, n+1):
    soma += num

print(f"A soma de 1 até {n} é: {soma}")
'''


# Exercício 4
'''
n = int(input("Digite um número 'n' para descobrir todos os divisores de 'n': "))

while n <= 0:
    print("Somente números positivos")
    n = int(input("Digite um número 'n' para descobrir todos os divisores de 'n': "))

for num in range(1, n+1):

    div = n % num

    if div == 0:
        print(num)
'''


# Exercício 5
'''
for n in range(2, 2001):
    primo = True

    for i in range(2, n):
        if n % i == 0:
            primo = False
            break

    if primo:
        print(n)
'''


# Exercício 6
'''
import random

n = int(input("Digite um número n: "))

while n <= 0:
    print("Digite um número positivo")
    n = int(input("Digite um número n: "))

vet_n = []

for num in range(n):
    vet_n.append(random.randint(0, n))

print(vet_n)
'''


# Exercício 7
'''
n = int(input("Digite um número n: "))

while n <= 0:
    print("Digite um número positivo")
    n = int(input("Digite um número n: "))

vet_n = []

for num in range(n):
    vet_n.append(num)

vet_n.sort(reverse=True)
print(vet_n)
'''


# Exercício 8
'''
A = [[4, 7, 1],
    [5, -3, 9]]
B = [[3, 0, 6],
     [2, 10, -2]]

C = []

for i in range(len(A)):
    for n in range(len(A[0])):
        soma = A[i][n] + B[i][n]
        C.append(soma)
print(C)
'''





