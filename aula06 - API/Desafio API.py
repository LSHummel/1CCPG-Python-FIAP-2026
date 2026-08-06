endpoints = ["/login", "/produtos", "/pedidos"]


status = [
[200, 200, 401, 200, 500],
[200, 200, 200, 200, 200],
[201, 500, 502, 201, 500]
]


acertos = 0
erros = 0
mais_erros = 0
endpoint_erro = 0


for x, end in enumerate(status):
    for i, erro in enumerate(end):

        if status[x][i] >= 200 and status[x][i] < 300:
            acertos += 1
        else:
            erros += 1



    if erros > mais_erros:
        mais_erros = erros
        endpoint_erro = x


    procentagem = 100*acertos/len(status[x])

    print(f"A procentagem de requisições bem-secedidas é de {procentagem:.0f}%")
    acertos = 0
    erros = 0
    sequencia_off = 0

print()
print(f"O endpoint com mais erro é o {endpoints[endpoint_erro]}")
print()

