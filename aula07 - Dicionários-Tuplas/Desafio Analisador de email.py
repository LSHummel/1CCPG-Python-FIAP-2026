emails = ['lucas.silva@gmail.com', 'maria.oliveira@outlook.com', 'joao.santos@yahoo.com', 'ana.costa@hotmail.com', 'pedro.almeida@gmail.com', 'juliana.rocha@icloud.com', 'gabriel.martins@outlook.com', 'camila.lima@gmail.com', 'rafael.gomes@yahoo.com', 'beatriz.ribeiro@hotmail.com', 'felipe.carvalho@gmail.com', 'larissa.fernandes@outlook.com', 'bruno.barros@gmail.com', 'amanda.teixeira@yahoo.com', 'mateus.correia@hotmail.com', 'isabela.mendes@gmail.com', 'vinicius.araujo@icloud.com', 'sofia.nascimento@outlook.com', 'daniel.cardoso@gmail.com', 'marina.pereira@yahoo.com', 'thiago.barbosa@hotmail.com', 'clara.moura@gmail.com', 'gustavo.dias@outlook.com', 'helena.freitas@gmail.com', 'eduardo.reis@yahoo.com', 'carolina.machado@hotmail.com', 'ricardo.nunes@gmail.com', 'bianca.tavares@icloud.com', 'leonardo.fonseca@outlook.com', 'isadora.castro@gmail.com', 'henrique.monteiro@yahoo.com', 'laura.vieira@hotmail.com', 'caio.miranda@gmail.com', 'leticia.coelho@outlook.com', 'andre.moraes@gmail.com', 'manuela.pinto@yahoo.com', 'diego.cavalcante@hotmail.com', 'gabriela.batista@gmail.com', 'murilo.campos@icloud.com', 'renata.duarte@outlook.com', 'arthur.azevedo@gmail.com', 'yasmin.farias@yahoo.com', 'otavio.macedo@hotmail.com', 'aline.borges@gmail.com', 'luciano.peixoto@outlook.com', 'sofia.vasconcelos@gmail.com', 'marcos.assis@yahoo.com', 'natalia.leal@hotmail.com', 'vinicius.souza@gmail.com', 'carla.figueiredo@icloud.com', 'alexandre.queiroz@outlook.com', 'monica.pires@gmail.com', 'rodrigo.dantas@yahoo.com', 'paula.aguiar@hotmail.com', 'samuel.andrade@gmail.com', 'aline.siqueira@outlook.com', 'igor.brito@gmail.com', 'tatiane.viana@yahoo.com', 'nicolas.magalhaes@hotmail.com', 'fernanda.sales@gmail.com', 'danilo.xavier@icloud.com', 'patricia.neves@outlook.com', 'lucas.monteiro@gmail.com', 'vanessa.torres@yahoo.com', 'erick.bezerra@hotmail.com', 'julia.martins@gmail.com', 'caue.ferreira@outlook.com', 'carol.assis@gmail.com', 'joaquim.ramos@yahoo.com', 'viviane.cabral@hotmail.com', 'wesley.moraes@gmail.com', 'ester.nogueira@icloud.com', 'marcelo.cunha@outlook.com', 'alice.faria@gmail.com', 'fabio.araujo@yahoo.com', 'debora.medeiros@hotmail.com', 'alan.teodoro@gmail.com', 'luana.pacheco@outlook.com', 'cesar.machado@gmail.com', 'renan.mattos@yahoo.com', 'elisa.brito@hotmail.com', 'brenda.martins@gmail.com', 'roberto.lopes@icloud.com', 'melissa.duarte@outlook.com', 'hugo.rangel@gmail.com', 'clara.sampaio@yahoo.com', 'emerson.assis@hotmail.com', 'lais.moreno@gmail.com', 'joel.santana@outlook.com', 'adriana.lemos@gmail.com', 'cristian.valente@yahoo.com', 'aline.novaes@hotmail.com', 'julio.castro@gmail.com', 'solange.rezende@icloud.com', 'marcio.tavares@outlook.com', 'eliane.martins@gmail.com', 'victor.henrique@yahoo.com', 'priscila.arantes@hotmail.com', 'sergio.batista@gmail.com', 'aline.carneiro@outlook.com']

d = dict()
for num in emails:
    username, domain = num.split('@')
    if domain not in d:
        d[domain] = 1
    else:
        d[domain] += 1
print(d)



emails_fiap = ['lucas.silva@gmail.com', 'maria.oliveira@fiap.com.br', 'joao.santos@yahoo.com', 'ana.costa@hotmail.com', 'pedro.almeida@gmail.com', 'juliana.rocha@icloud.com', 'felipe.carvalho@fiap.com.br', 'larissa.fernandes@outlook.com', 'bruno.barros@fiap.com.br']
t = ()

for num, email in enumerate(emails_fiap):
    username, domain = email.split('@')

    t = username


print(t)
