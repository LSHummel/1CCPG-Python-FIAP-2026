print("Ola Mundo")


print(7 + 4)
print("7 + 4")
print("7" + "4") # Concatenando strings

# Comentário de 1 linha
'''
    Comentários de 
    Multiplas
    linhas
'''

# Variaveis
nome = "Seiji" # str
idade = 17 # int
peso = 60.7 # float

print(nome, idade, peso)
print(f"Olá, {nome}!!!")


#input -- simulação de um forms no cmd

nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
peso = float(input("Digite o seu peso: "))
print(nome, idade, peso)
print(idade + 1)

ano_nascimento = 2008
ano_atual = 2026
idade = ano_atual - ano_nascimento
print(f"Sua idade é: {idade}")