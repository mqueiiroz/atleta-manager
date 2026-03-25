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
    
atleta1 = Atleta('Matheus', 21, 'Defensor')
atleta2 = Atleta('Joao', 17, 'Atacante')
print(atleta1)
print(atleta2)
