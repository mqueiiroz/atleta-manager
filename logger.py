from datetime import datetime

def registrar_evento(mensagem):

    timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    linha_log = f'[{timestamp}] {mensagem}\n'
    
    with open('historico.txt', 'a', encoding='utf-8') as arquivo:
        arquivo.write(linha_log)