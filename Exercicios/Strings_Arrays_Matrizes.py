# Bibliotecas

import random
from time import process_time_ns

# Escreva um algoritmo que recebe um número inteiro n > 0, cria um vetor de números reais com n posições e preenche o vetor com n números aleatórios reais.
# Depois de preenchido o vetor, imprima na tela todos os números gerados.
'''
n = int(input("Digite um número: "))

while n < 0:
    n = int(input("Digite um número positivo: "))

numeros = [random.randint(1, n) for _ in range(n)]

print(numeros)
'''

# Considere uma turma de n alunos onde desejamos calcular a média das notas da prova semestral e saber quantas notas estão iguais, acima e abaixo dessa média.
# Escreva um algoritmo que lê um inteiro n representando a quantidade de alunos e cada uma das n notas e mostra a média da turma, quantas notas são iguais, acima e abaixo da média da turma.

alunos = int(input("Digine o número de alunos da turma: "))

i = 0
turma = []
while i < alunos:
    nota = int(input("Digite a nota dos alunos separadamente: "))
    turma.append(nota)
    i=i+1

turma.sort()
media = sum(turma) / len(turma)
print(f"A média dos alunos é de {media:.2f}")

nota_baixa = 0
nota_alta = 0
nota_media = 0
nota_igual = 0
for indice in range(alunos):
    if turma[indice] < media:
        nota_baixa = nota_baixa + 1
    if turma[indice] > media:
        nota_alta = nota_alta + 1
    if turma[indice] == media:
        nota_media = nota_media + 1
    for igual in range(alunos):
        if turma[indice] == turma[igual]:
            nota_igual = nota_igual + 1
print(f"A turma tem {nota_baixa} notas abaixo da média")
print(f"A turma tem {nota_alta} notas acima da média")
print(f"A turma tem {nota_media} notas na média")
print(f"A turma tem {nota_igual} notas iguais")



