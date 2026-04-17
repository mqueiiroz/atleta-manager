from logger import registrar_evento

class Atleta:
    lista_de_posicao = ['Defensor','Meio-Campista','Atacante']
    def __init__ (self, id,nome,idade,posicao):
        self.nome = nome
        self.idade = idade
        self.id = id
        registrar_evento(f'Atleta {self.nome}')
        if posicao in self.lista_de_posicao:
            self.posicao = posicao
        else:
            raise ValueError("Essa posição não existe")

    def __str__ (self):
        return f'Id:{self.id} | Nome: {self.nome} | Idade: {self.idade} | Posição: {self.posicao}'