import json

class Atleta:
    def __init__ (self, id,nome,idade,posicao):
        self.nome = nome
        self.idade = idade
        self.id = id
        self.lista_de_posicao = ['Defensor','Meio-Campista','Atacante']
        if posicao in self.lista_de_posicao:
            self.posicao = posicao
        else:
            raise Exception ('Essa posição não existe')


    def __str__ (self):
        return f'Id:{self.id} | Nome: {self.nome} | Idade: {self.idade} | Posição: {self.posicao}'

class Time:
    times_criados = []
    def __init__(self, nome):
        self.nome = nome
        self.lista_de_atletas = []
        nome_verificado = nome.strip().capitalize()
        if self.existe_time(nome_verificado):
            raise ValueError ('Ja existe esse time')
        self.nome = nome_verificado
        Time.times_criados.append(self)

    @classmethod
    def existe_time(cls,nome_verificado):
        for time in cls.times_criados:
            if time.nome == nome_verificado:
                return True
        return False
    
    @staticmethod
    def verificar_idade(idade):
            if idade > 16:
                return True
            return False        
    
    def adicionar_atleta(self,atleta):
        if self.verificar_idade(atleta.idade):
            self.lista_de_atletas.append(atleta)
        else:
            raise ValueError('Idade invalida')
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

    def salvar_dados(self):
        self.dados = {
            atleta.id : atleta.__dict__ for atleta in self.lista_de_atletas    
            }
        print(self.dados)
        with open('data/dados_dos_atletas.json','w',encoding='utf--8') as f:
            json.dump(self.dados,f)
        
    def carregar_dados(self):
        with open('data/dados_dos_atletas.json','r',encoding='utf--8') as f:
            dados_do_json = json.load(f)
            for k,v in dados_do_json.items():
                novo_atleta = Atleta(
                    v['id'],
                    v['nome'],
                    v['idade'],
                    v['posicao'],
                )
                self.lista_de_atletas.append(novo_atleta)

time1 = Time('Ceará')
atleta1 = Atleta('01','Matheus',20,'Defensor')
time1.adicionar_atleta(atleta1)
atleta2 = Atleta('02' ,'Mauricio',30,'Defensor')
time2 = Time('Ceará')
time1.adicionar_atleta(atleta2)
time1.carregar_dados()
time1.salvar_dados()

