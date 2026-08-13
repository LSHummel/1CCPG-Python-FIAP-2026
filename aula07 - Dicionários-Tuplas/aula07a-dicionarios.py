eng2sp = dict()
print(eng2sp)

eng2sp['one'] = 'uno'
print(eng2sp)

eng2sp = {
    'one': 'uno',
    'two': 'dos',
    'three': 'tres'
}

print(eng2sp)
print(eng2sp['two'])

print('uno' in eng2sp)

valores = eng2sp.values()
print('uno' in valores)

def count_letters(s): # s ---> string
    d = dict() # Criacao do dicionario
    for c in s: # c ---> caracter
        if c not in d: # ve se existe uma chave para a letra
            d[c] = 1 # Cria uma chave pro dicionario
        else:
            d[c] += 1 # Vai adiciona mais 1 no contador
    return d

dict_contagem = count_letters("ovo")
print(dict_contagem)










