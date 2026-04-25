# Faça um programa que exiba a mensagem “Olá, Mundo”.
# Essa mensagem deverá ser exibida repetidamente.
# Ao final de toda iteração da repetição, você deve perguntar ao usuário se ele deseja exibir a mensagem novamente.
# Se sim, exiba novamente. Senão, saia do loop e exiba a mensagem “Fim”.
'''
oi = "sim"

while oi.lower() == "sim":
    print("Olá Mundo")
    oi = input("Quer ver a mensagem novamente? ")
print("Fim")
'''


#  Contagem de 0 a 100 pulando de 10 em 10.
'''
for n in range(0, 101, 10):
    print(n)
'''


# Faça um programa que receba um número n
# Exiba a tabuada deste número do 0 ao 25.
# Utilize laços de repetição
'''
n = int(input("Digite um número n: "))

i = -1
while i < 25:
    i += 1
    tabuada = n * i
    print(f"{n} X {i} = {tabuada}")
'''


# Faça um programa que receba 5 valores digitados pelo usuário e, ao final, informe qual é a soma deles.
'''
i = 5
soma = 0
while i > 0:
    n = int(input("Digite um numero: "))
    i -= 1
    soma += n

print(f"Os cinco números somados dão {soma}")
'''


# Faça um programa que receba 5 valores digitados pelo usuário e, ao final, informe qual é o maior deles.
'''
i = 5
maior = 0
while i > 0:
    n = int(input("Digite um numero: "))
    i -= 1
    if n > maior:
        maior = n
print(f"O maior número é {maior}")
'''


# Faça um programa capaz de exibir todos os valores pares entre 2 e um valor fornecido pelo usuário.
'''
n = int(input("Digite um número: "))

for n in range(2, n, 2):
        print(n)
'''


# Escreva um programa que dado um inteiro n positivo calcula e imprime a soma de todos os números inteiros entre 1 e n.
# Valide a entrada do usuário, só aceite números positivos!!
'''
n = int(input("Digite um positivo número: "))
soma = 0

while n < 0:
    n = int(input("Digite novamente um número positivo: "))

for n in range(1, n+1):
    print(n)
while n > 1:
    soma += n
    n -= 1
print(f"A soma dos números é: {soma}")
'''


# Escreva um algoritmo que recebe um inteiro positivo n e imprime todos os divisores positivos de n.
# Utilize o laço for.
'''
n = int(input("Digite um número n positivo: "))
while n < 0:
    n = int(input("Digite novamente o n positivo: "))

for i in range(1, n+1):
    if n % i == 0:
        print(i)
'''


# Determine e mostre todos os números primos no intervalo de 2 a 2000.
'''
for n in range(2, 2001):
    for i in range(2, 2001):
        if n%i == 0 :
            print(i)
'''
n = int(input("Digite um número n positivo: "))
while n < 0:
    n = int(input("Digite novamente o n positivo: "))

for i in range(1, n+1):
    if n % i == 0:
        print(i)