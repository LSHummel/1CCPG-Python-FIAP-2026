'''
numero = int(input("Digite um número: "))

novo_numero = numero % 2

if novo_numero == 0:
    print("O número é par")
else:
    print("O número é impar")
'''



'''
numero_1 = int(input("Digite qualquer número de 0 a 100: "))
numero_2 = int(input("Digite qualquer número de 0 a 100, novamente: "))

if numero_1 > numero_2:
    print(f"O maior número é {numero_1}")
elif numero_1 == numero_2:
    print("Os números são identicos")
else:
    print(f"O maior número é {numero_2}")
'''


'''
nota_1 = float(input("Digite sua primera nota: "))
nota_2 = float(input("Digite sua segunda nota: "))
nota_3 = float(input("Digite sua terceira nota: "))
nota_4 = float(input("Digite sua quarta nota: "))

media = (nota_1 + nota_2 + nota_3 + nota_4) / 4

if media >= 7:
    print(f"Sua média foi: {media:.2f}, você foi Aprovado!")
elif 7 > media >=5:
    print(f"Sua média foi: {media:.2f}, você esá de Recuperação!")
else:
    print(f"Sua média foi: {media:.2f}, você está Reprovado!")
'''


'''
numero_1 = int(input("Digite um número: "))
numero_2 = int(input("Digite um número: "))

if numero_1 >= numero_2:
    multiplo = numero_1 % numero_2
else:
    multiplo = numero_2 % numero_1

if multiplo == 0:
    print("Os números são multiplos")
else:
    print("Os números não são multiplos")
'''

'''
numero_1 = float(input("Digite um número: "))
numero_2 = float(input("Digite um número: "))
operador = input("Digite um operador matemático (+, -, /, *): ")

if operador == "+":
    conta = numero_1 + numero_2
elif operador == "-":
    conta = numero_1 - numero_2
elif operador == "/":
    conta = numero_1 / numero_2
elif operador == "*":
    conta = numero_1 * numero_2

print(f"A conta resulta em: {conta:.2f}")
'''

'''
nascimento = int(input("Digite seu ano de nascimento: "))

idade = 2026 - nascimento

if idade >= 18 | idade <= 70:
    print("Você é obigado a votar este ano!")
elif idade < 16:
    print("Você não pode votar este ano!")
else:
    print("Você não é obrigado a votar este ano!")
print(idade)
'''

'''
salario = float(input("Informe o seu salário: R$"))

if salario <= 280:
    reajuste  = 1.2 * salario
    percentual = 20
    aumento = 0.2 * salario
elif salario > 280 and salario <= 700:
    reajuste = 1.15 * salario
    percentual = 15
    aumento = 0.15 * salario
elif salario > 700 and salario <= 1500:
    reajuste = 1.10 * salario
    percentual = 10
    aumento = 0.1 * salario
elif salario > 1500:
    reajuste = 1.05 * salario
    percentual = 5
    aumento = 0.05 * salario

print(f"Salario antes do reajuste: R${salario:.2f}")
print(f"Percentual de aumento: {percentual}%")
print(f"Valor do aumento: R${aumento:.2f}")
print(f"Salario depois do reajuste: R${reajuste:.2f}")
'''

'''
codigo_o = int(input("Informeo código do estado de origem o caminhão(1 a 5): "))
peso = float(input("Informe o pedo do seu caminhão em toneladas: "))
codigo_c = int(input("Informe o código da carga(10 a 40): "))

peso_kg = peso * 1000

if 10 <= codigo_c <= 20:
    preco = peso_kg * 100
elif 21 <= codigo_c <= 30:
    preco = peso_kg * 250
elif 31 <= codigo_c <= 40:
    preco = peso_kg * 340

if codigo_o == 1:
    imposto = preco * 0.35
elif codigo_o == 2:
    imposto = preco * 0.25
elif codigo_o == 3:
    imposto = preco * 0.15
elif codigo_o == 4:
    imposto = preco * 0.05
elif codigo_o == 5:
    imposto = preco * 0

valor_total = preco + imposto

print(f"Peso do caminhão: {peso_kg:.2f}Kg")
print(f"Preço da carga: R${preco:.2f}")
print(f"Valor do imposto: R${imposto:.2f}")
print(f"Valor total: R${valor_total:.2f}")
'''

'''
lado_1 = float(input("Medida do lado do triângulo: "))
lado_2 = float(input("Medida do lado do triângulo: "))
lado_3 = float(input("Medida do lado do triângulo: "))


if lado_1 > lado_2 > lado_3:
    A = lado_1
    B = lado_2
    C = lado_3
elif lado_1 > lado_3 > lado_2:
    A = lado_1
    B = lado_3
    C = lado_2
elif lado_2 > lado_1 > lado_3:
    A = lado_2
    B = lado_1
    C = lado_3
elif lado_2 > lado_3 > lado_1:
    A = lado_2
    B = lado_3
    C = lado_1
elif lado_3 > lado_1 > lado_2:
    A = lado_3
    B = lado_1
    C = lado_2
elif lado_3 > lado_2 > lado_1:
    A = lado_3
    B = lado_2
    C = lado_1
elif lado_1 == lado_2 == lado_3 or (lado_3 == lado_2) < lado_1:
    A = lado_1
    B = lado_2
    C = lado_3
elif (lado_1 == lado_2) < lado_3 or (lado_1 == lado_3) > lado_2:
    A = lado_3
    B = lado_1
    C = lado_2
elif (lado_1 == lado_3) < lado_2 or (lado_1 == lado_2) > lado_3:
    A = lado_2
    B = lado_3
    C = lado_1
elif (lado_3 == lado_2) > lado_1:
    A = lado_3
    B = lado_2
    C = lado_1


print("Classificção do Triângulo com base nos ângulos")
if A >= (B + C):
    print("Os lados não formam um Triângulo\n")
elif A**2 == (B**2 + C**2):
    print("Os ângulos formam um Triângulo Retângulo\n")
elif A**2 > (B**2 + C**2):
    print("Os ângulos formam um Triângulo Obtusângulo\n")
elif A**2 < (B**2 + C**2):
    print("Os ângulos formam um Triângulo Acutângulo\n")
else:
    print("ERRO!")

print("Classificação do Triângulo com base nos lados")
if A == B == C:
    print("Os lados do Triângulo formam um Triângulo Equilatero")
elif A == B != C or A == C != B or B == C != A:
    print("Os lados do Triângulo formam um Triângulo Isosceles")
else:
    print("Não possui classificação com base nos lados")
'''