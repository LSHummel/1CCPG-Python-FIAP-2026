temperaturas = [[28, 31, 34, 33], [25, 27, 29, 28], [32, 35, 36, 34], [24, 26, 25, 27]]

maior = 0
num_sala = 1
critico = 0
sala_max = 0

for sala in temperaturas:
    print(f"Sala {num_sala}")
    print(f"Média: {sum(sala)/len(sala)}")
    maior = 0
    for temp in sala:
        if temp >= 33:
            maior += 1
    print(f"Registro crítico: {maior}")
    print()


    if maior > critico:
        critico = maior
        sala_max = num_sala
    num_sala += 1
print(f"Sala com maior risco: Sala {sala_max}")







