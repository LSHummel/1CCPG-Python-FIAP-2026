emails = ['lucas.silva@gmail.com', 'maria.oliveira@fiap.com.br', 'joao.santos@yahoo.com', 'ana.costa@hotmail.com', 'pedro.almeida@gmail.com', 'juliana.rocha@icloud.com', 'felipe.carvalho@fiap.com.br', 'larissa.fernandes@outlook.com', 'bruno.barros@fiap.com.br', 'amanda.teixeira@yahoo.com', 'mateus.correia@hotmail.com']

d = dict()
t = ()
tl = ()
for num in emails:
    username, domain = num.split('@')
    if domain not in d:
        d[domain] = 1
    else:
        d[domain] += 1

    tf = list(t)
    tf.append(username)
    t = tuple(tf)

print(f"Quantidade de emails por dominio: \n{d}\n")
print(f"Lista de úsuarios {t}")

tf = list(t)
tf[0], tf[len(emails)-1] = tf[len(emails)-1], tf[0]
t = tuple(tf)

print(f"Após troca de posição {t}")
