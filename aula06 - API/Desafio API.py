endpoints = ["/login", "/produtos", "/pedidos"]

status = [
[200, 200, 401, 200, 500],
[200, 200, 200, 200, 200],
[201, 500, 502, 201, 500]
]

# Variaveis
acertos = 0
erros = 0
mais_erros = 0
endpoint_erro = 0
sequencias = [0, 0, 0]

# Verificação de erros
for x, end in enumerate(status):
    for i, codigo in enumerate(end):

        if codigo >= 200 and codigo < 300:
            acertos += 1
        else:
            erros += 1
        # Contagem de erros seguidos
        if i < len(end) - 1:
            if codigo >= 400 and end[i + 1] >= 400:
                sequencias[x] = 1

    # Verificação de endpoint com mais erros
    if erros > mais_erros:
        mais_erros = erros
        endpoint_erro = x

    # Resposta em porcentagem
    porcentagem = 100*acertos/len(status[x])
    print(f"A procentagem de requisições bem-secedidas é de {porcentagem:.0f}%")
    acertos = 0
    erros = 0

    # Resposta da análise
    if sequencias[x] == 1:
        print("Crítico")
    elif porcentagem >= 80:
        print("Estável")
    else:
        print("Instável")

# Resposta do endpoint com mais erros
print()
print(f"O endpoint com mais erro é o {endpoints[endpoint_erro]}")
print()