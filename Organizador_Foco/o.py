import sys
import os
import shutil
from datetime import datetime

sys.stdout.reconfigure(encoding='utf-8')

environmental = os.environ
username = environmental['USERNAME']

downloads_path = rf'C:\Users\{username}\Downloads'
downloads_foco_path = rf'C:\Users\{username}\Downloads_Foco'
arquivos_path = rf'C:\Users\{username}\Downloads_Foco\Arquivos'
organizacao_path = rf'C:\Users\{username}\Downloads_Foco\Organização'

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

if not os.path.isdir(downloads_foco_path):
    os.makedirs(downloads_foco_path)
    os.makedirs(arquivos_path)
    os.makedirs(organizacao_path)

for file in os.listdir(downloads_path):
    file_path = f'{downloads_path}\{file}'
    new_file_path = f'{arquivos_path}\{file}'
    
    # Se o arquivo já existir no destino, renomear
    if os.path.exists(new_file_path):
        filename, file_extension = os.path.splitext(file)
        num = 1
        while os.path.exists(new_file_path):
            new_file_name = f"{filename} ({num}){file_extension}"
            new_file_path = f'{arquivos_path}\{new_file_name}'
            num += 1
    
    shutil.move(file_path, new_file_path)

for file in os.listdir(arquivos_path):
    filename, file_extension = os.path.splitext(file)
    file_path = f'{arquivos_path}\{file}'
    num = 1

    timestamp_criacao = os.path.getctime(rf'{arquivos_path}\{file}')

    data_criacao = datetime.fromtimestamp(timestamp_criacao)

    ano_criacao = str(data_criacao.year)
    mes_criacao = meses[data_criacao.month]

    # Para pastas
    if os.path.isdir(file_path):
        folder = rf'{organizacao_path}\{ano_criacao}\{mes_criacao}\PASTAS'
    
    # Para arquivos diversos
    else:    
        folder = rf'{organizacao_path}\{ano_criacao}\{mes_criacao}\{file_extension[1:].upper()}'

    # Criar pasta
    if not os.path.isdir(folder):
        os.makedirs(folder)

    # Lidar com arquivos/pastas de nomes iguais
    while file in os.listdir(folder):
            
        file = f"{filename} ({num_while_2}){file_extension}"
        new_file_path = f'{arquivos_path}\{file}'
        os.rename(file_path, new_file_path)
        file_path = new_file_path
        num_while_2 = num_while_2 + 1

    # Mova arquivo/pasta pra pasta determinada
    shutil.move(f'{file_path}', f'{folder}')
