from models import Atleta,Time

time1 = Time('Ceará')
atleta1 = Atleta('01','Matheus',20,'Defensor')
time1.adicionar_atleta(atleta1)
atleta2 = Atleta('02' ,'Mauricio',30,'Defensor')
time2 = Time('Vasco')
time1.adicionar_atleta(atleta2)
time1.salvar_dados()

