import sys
import os
from datetime import datetime
import shutil

sys.stdout.reconfigure(encoding='utf-8')

environmental = os.environ
username = environmental['USERNAME']

downloads_path = rf'C:\Users\{username}\Downloads'
downloads_foco_path = rf'C:\Users\{username}\Downloads_Foco'

meses = {
    1: 'Janeiro',
    2: 'Fevereiro',
    3: 'Março',
    4: 'Abril',
    5: 'Maio',
    6: 'Junho',
    7: 'Julho',
    8: 'Agosto',
    9: 'Setembro',
    10: 'Outubro',
    11: 'Novembro',
    12: 'Dezembro'
}

for file in os.listdir(downloads_path):
    filename, file_extension = os.path.splitext(file)

    timestamp_criacao = os.path.getctime(rf'{downloads_path}\{file}')

    data_criacao = datetime.fromtimestamp(timestamp_criacao)

    ano_criacao = str(data_criacao.year)
    mes_criacao = meses[data_criacao.month]

    # Ver se a pasta do ano foi criada
    ano_path = rf'{downloads_foco_path}\Organização\{ano_criacao}'
    if not os.path.isdir(ano_path):
        print(f'Criando diretório: {ano_path}')
        os.mkdir(ano_path)

    # Verifica se a pasta do mes foi criada 
    mes_path = rf'{ano_path}\{mes_criacao}'
    if not os.path.isdir(mes_path):
        print(f'Criando diretório: {mes_path}')
        os.mkdir(mes_path)
    
    shutil.move(rf'{downloads_path}\{file}', rf'{mes_path}\{file}')