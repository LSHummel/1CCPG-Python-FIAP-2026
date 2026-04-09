#função sem retorno sem parametro
def print_lytics():
    print("I ain't gonna live forever")
    print("I just want to live while I'm alive")

print_lytics()
print_lytics()

#função sem retorno com parametro
def boas_vindas(nome):
    print(f"Olá, {nome}!! Seja bem_vindo")

nome_digitado = input("Digite seu nome: ")
boas_vindas(nome_digitado)

#função com retorno com arametro
def soma(num_a, num_b):
    soma = num_a + num_b
    return soma

print(soma(10, 5)) #com print(), ele exibe
type(nome_digitado) #apenas armazena


