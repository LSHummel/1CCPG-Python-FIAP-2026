endpoints = ["/login", "/produtos", "/pedidos"]


status = [
[200, 200, 401, 200, 500],
[200, 200, 200, 200, 200],
[201, 500, 502, 201, 500]
]


ok = 0
off = 0
mais_off = 0


for x, end in enumerate(status):
    print()
    for i, erro in enumerate(end):

        if status[x][i] >= 200 and status[x][i] < 300:
            ok += 1

        else:
            off += 1

    procentagem = 100*ok/len(status[x])

    print(f"A procentagem de requisições bem-secedidas é de {procentagem:.0f}%")
    ok = 0
    off = 0

