class Atleta:
    def __init__ (self, nome,idade,posicao):
        self.nome = nome
        self.idade = idade
        self.lista_de_posicao = ['Defensor','Meio-Campista','Atacante']
        if posicao in self.lista_de_posicao:
            self.posicao = posicao
        else:
            raise Exception ('Essa posição não existe')


    def __str__ (self):
        return f'Nome: {self.nome} | Idade: {self.idade} | Posição: {self.posicao}'

class Time:
    def __init__(self, nome):
        self.nome = nome
        self.lista_de_atletas = []

    def adicionar_atleta(self,atleta):
        self.lista_de_atletas.append(atleta)

    def __str__(self):
        nomes = [atleta.nome for atleta in self.lista_de_atletas]
        return f'Time: {self.nome} :{nomes}'

    def remover_atleta(self,nome_procurado):
        for atleta in self.lista_de_atletas:
            if atleta.nome == nome_procurado:
                self.lista_de_atletas.remove(atleta)
                break
        else:
            print(f'Não foi encontrado Ninguem com esse nome :{nome_procurado}')

    def listar_elenco(self,time):
        for atleta in self.lista_de_atletas:
            nome = atleta.nome
            idade = atleta.idade
            posicao = atleta.posicao
        print(f'{nome} | {idade} | {posicao}')
        

time1 = Time('Ceará')
atleta1 = Atleta('Matheus',20,'Defensor')
time1.adicionar_atleta(atleta1)
atleta2 = Atleta('Mauricio',30,'Defensor')


time1.adicionar_atleta(atleta2)
time1.remover_atleta('Mauricio')
time1.remover_atleta('Joao')
print(time1)

time1.listar_elenco('Ceará')

