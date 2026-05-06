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
'''
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
print(f"A turma tem {nota_baixa} notas abaixo da média")
print(f"A turma tem {nota_alta} notas acima da média")
print(f"A turma tem {nota_media} notas na média")
'''

# Faça um programa que tenha 2 vetores. Um vetor para os meses e outros para a quantidade de dias para cada mês.
# Seu programa deve exibir mensagens da seguinte forma:
 # O Mês de Jan tem 31 dias ao tod
 # O mês de Fev tem 28 dias ao tod
 # O mês de Mar tem 31 dias ao tod
 # ...
 # O mês de Dez tem 31 dias ao tod
'''
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
dias = ["31", "28", "31", "30", "31", "30", "31", "31", "30", "31", "30", "31"]

for i in range(12):
    if i == i:
        print(f"O mês de {meses[i]} tem {dias[i]} dias ao todo.")
'''

# Escreva um algoritmo que lê um número inteiro n, cria um vetor de inteiros de tamanho n, faz a leitura de um conjunto de n números inteiros armazenando-os no vetor e depois calcula a somatória dos números contidos no vetor.
# Dica: note que a somatória deverá ser feita após o vetor estar preenchido
'''
n = int(input("Digite quantos números inteiros quer somar: "))

soma = []
i = 0
while i < n:
    num_soma = int(input("Digite os números que deseja somar: "))
    soma.append(num_soma)
    i = i + 1

resultado = sum(soma)
print(f"A soma dos números é: {resultado}")
'''

# Escreva um algoritmo que recebe uma lista de nomes e imprime os nomes na ordem inversa a da leitura.
# A lista termina quando o usuário aperta o Enter sem que nenhum nome tenha sido digitado.
'''
nomes = input("Digite uma lista de nomes: ")

separado = nomes.split()
separado.sort(reverse=True)
print(separado)
'''

# Escreva um algoritmo que lê um número inteiro n > 0 e preenche um vetor de caracteres de n posições.
# Depois de preencher o vetor, você deverá inverter o seu conteúdo, ou seja, trocar o conteúdo da primeira posição (0) com a ´ultima (n − 1) a segunda com a penúltima e assim por diante até que o vetor esteja invertido.
'''
n = int(input("Digite a quantidade de numeros que deseja dentro do vetor: "))
while n < 0:
    n = int(input("Digite uma quantidade maior que zero: "))
    
print("Lista de números aleatoria")
lista_num_aleatorios = [random.randint(1, n) for _ in range(n)]
print(lista_num_aleatorios)
lista_num_aleatorios.reverse()
print(lista_num_aleatorios)

print()

print("Lista de números em ordem")
lista_num = []
for i in range(n):
    lista_num.append(i)
print(lista_num)
lista_num.reverse()
print(lista_num)
'''

# Crie um programa com uma matriz 3x4
 # 3 linhas
 # 4 colunas
# Atribua valores aleatórios à todas posições da matriz.
# Exiba essa matriz.
'''
favoritas = [
    ["Comida", "Cor", "Lugar", "Hobbie"],
    ["Hamburguer", "Azul", "Praia", "Croche"],
    ["Nhoque", "Roxo", "Quarto", "Filme"]
]
for favorito in favoritas:
    print(favorito)
'''

# Faça um programa que realize a soma de duas matrizes, com mesmas dimensões. Seu programa deve ter 2 matrizes A e B de números inteiros. A terceira matriz deve ser a soma de A com B.
'''
n = 10
A = [
    [random.randint(1, n) for _ in range(3)],
    [random.randint(1, n) for _ in range(3)]
]
B = [
    [random.randint(1, n) for _ in range(3)],
    [random.randint(1, n) for _ in range(3)]
]
C = [
    [A[0][0]+B[0][0], A[0][1]+B[0][1], A[0][2]+B[0][2]],
    [A[1][0]+B[1][0], A[1][1]+B[1][1], A[1][2]+B[1][2]]
]
print("A")
for a in A:
    print(a)
print()
print("B")
for b in B:
    print(b)
print()
print("A + B = C")
for c in C:
    print(c)
'''