from models import Time
import random
from logger import registrar_evento

class Partida:
    def __init__(self, time_casa,time_fora):
        self.time_casa = time_casa
        self.time_fora = time_fora

    def calcular_forca(self,time):
            if len(time.lista_de_atletas) == 0:
                 return 0
            else:
                return len(time.lista_de_atletas) * 10
        
    def jogar(self):
        forca_casa = self.calcular_forca(self.time_casa)
        forca_fora = self.calcular_forca(self.time_fora)            

        gols_casa = random.randint(0,3) + (1 if forca_casa > forca_fora else 0)
        gols_fora = random.randint(0,3) + (1 if forca_fora > forca_casa else 0)

        print(f'{self.time_casa.nome} {gols_casa} x {gols_fora} {self.time_fora.nome}')
        msg = f"Partida realizada: {self.time_casa.nome} {gols_casa} x {gols_fora} {self.time_fora.nome}"
        registrar_evento(msg)

        if gols_casa > gols_fora:
             print(f'Vencedor : {self.time_casa.nome}')
        elif gols_fora > gols_casa:
             print(f'Vencedor {self.time_fora.nome}')
        else:
             print('Empate')

    