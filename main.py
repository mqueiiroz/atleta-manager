from models import Atleta,Time,Partida

time1 = Time('Ceará')
time2 = Time('Vasco')
atleta1 = Atleta('01','Matheus',20,'Defensor')
time1.adicionar_atleta(atleta1)
atleta2 = Atleta('02' ,'Mauricio',30,'Defensor')
time2.adicionar_atleta(atleta2)
atleta3 = Atleta('03','Caio',21,'Atacante')
time1.adicionar_atleta(atleta3)
time1.salvar_dados()
time2.salvar_dados()

partida = Partida(time1,time2)
partida.jogar()