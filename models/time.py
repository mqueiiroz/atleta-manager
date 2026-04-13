import json
from .atleta import Atleta

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