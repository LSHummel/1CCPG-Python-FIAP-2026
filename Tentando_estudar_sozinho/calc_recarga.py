import json

with open("dados_recarga.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

ultimo = dados[-1]


ener_consumida = int(ultimo["kwh"]) - int(ultimo["kwh"]) * (int(ultimo["porcentagem"]) / 100)

tempo = ener_consumida / 50

tempo_h = int(ener_consumida / 50)

tempo_m = (tempo - tempo_h) * 60

valor_total = ener_consumida * 2 + 1.80






                # // Energia consumida pelo carro
                # ener_consumida[carro_atual] = total_kwh[carro_atual] - total_kwh[carro_atual] * (porcentagem[carro_atual] / 100);

                # // Tempo da recarga em horas
                # tempo[carro_atual] = (ener_consumida[carro_atual] / 50) * fator_tempo;

                # // Tempo da recarga em horas inteiro
                # tempo_hora[carro_atual] = (int)(ener_consumida[carro_atual] / 50) * fator_tempo;

                # // Minutos da recarga
                # tempo_min[carro_atual] = (tempo[carro_atual] - tempo_hora[carro_atual]) * 60;

                # // Custo total
                # valor_total[carro_atual] = (ener_consumida[carro_atual] * 2 + 1.80) * fator_horario;

                # // Porcentagem que será carregada
                # porcentagem_f[carro_atual] = 100 - porcentagem[carro_atual];
