print()
print("Exercícios para treinar:")
print()

print("1) Calcule a área de um círculo com raio 5. Use a fórmula: área = π * raio^2. (Dica: você pode usar 3.14159 como valor aproximado de π).")

def calc_A_Circulo(r):
    A = 3.14159 * r**2
    return A
print(f'R: A área do circulo é {float(calc_A_Circulo(5))} U.C')

print()
print()

print("2) Converta uma temperatura de Fahrenheit para Celsius. A fórmula de conversão é: Celsius = (Fahrenheit - 32) * 5/9.")

def calc_T_Celsius(f):
    C = (f - 32) * 5/9
    return C
print(f'R: A Conversão de 93 Fahrenheit para Celsius é de {int(calc_T_Celsius(93))}')

print()
print()

print("3) Você comprou 3 livros por R$ 25 cada e 2 canetas por R$ 5 cada. Calcule o total gasto.")

T = 3*25 + 2*5
print(f'R: O total gasto foi de R$ {T:.2f}')

print()
print()

print("4) Um carro percorreu 150 km a uma velocidade média de 60 km/h. Quanto tempo (em horas) o carro levou para percorrer essa distância?")

t = 60 / 150
print(f'R: O tempo que o carro levou para percorrer a distância foi de {float(t)} horas')

print()
print()

print("5) Leia 2 valores A e B, que correspondem a 2 notas de um aluno. A seguir calcule e informe a média aritmética do aluno.")
def calc_Média(a,b):
    M = (a+b)/2
    return M
print(f'R: A média da nota do aluno é de {float(calc_Média(8,6)):.2f}')

print()
print()

print("6) Leia 2 valores A e B, que correspondem a 2 notas de um aluno. A seguir calcule e informe a média ponderada do aluno, sabendo que a nota A tem peso 4 e a nota B tem peso 6.")

def calc_M_Peso(a,b):
    MP = (a*4 + b*6) / 10
    return MP
print(f'R: A média do aluno, com peso 4 e 6 nas p1 e p2, respectivamente, é de {float(calc_M_Peso(5, 3)):.2f}')

print()
print()

print("7) Neste problema, deve-se ler o nome de uma peça que chamaremos de peça1, o número de peças1 que o usuário quer, o valor unitário de cada peça1, o nome de uma peça2, o número de peças2 e o valor unitário de cada peça2. Após, calcule e mostre o valor a ser pago.")

Qc = int(input('Quantas canetas você quer ?'))
Ql = int(input('Quantps lapís você quer ?'))

P = (Qc*5) + (Ql*6)

print(f'R: O total da compra é de R$ {float(P):.2f}')

print()
print()

print("8) Crie um programa que receba o valor do produto e valor pago. Calcule o troco a ser pago. O valor do troco deve ser exibido no terminal.")

Valor_da_Compra = int(input('Qual o valor da compra?'))
Valor_Pago = int(input('Qual o valor pago?'))

Troco = Valor_Pago - Valor_da_Compra

print(f'R: O troco foi de R$ {Troco:.2f}')
