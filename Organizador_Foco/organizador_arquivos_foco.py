import sys
import os
import shutil

sys.stdout.reconfigure(encoding='utf-8')

environmental = os.environ
username = environmental['USERNAME']

#for file in os.listdir(rf'C:\Users\{username}\Downloads'):
#    shutil.move(rf'C:\Users\{username}\Downloads\{file}')

downloads_path = rf'C:\Users\{username}\Downloads_Foco'
arquivos_path = rf'C:\Users\{username}\Downloads_Foco\Arquivos'

if not os.path.isdir(downloads_path):
    os.mkdir(downloads_path)
    os.mkdir(arquivos_path)
    os.mkdir(rf'{downloads_path}\Organização')


for file in os.listdir(downloads_path):
    filename, file_extension = os.path.splitext(file)
    file_path = f'{downloads_path}\{file}'
    num = 1

    # bullshit
    if filename == "Arquivos" or filename == "Organização":
        continue

    # Para pastas
    if os.path.isdir(file_path):
        folder = f'{arquivos_path}\PASTAS'
        
    # Para arquivos diversos
    else:    
        folder = f'{arquivos_path}\{file_extension[1:].upper()}'
    
    # Criar pasta
    if not os.path.isdir(folder):
        os.mkdir(folder)

    # Lidar com arquivos/pastas de nomes iguais
    while file in os.listdir(folder):
            
        file = f"{filename} ({num}){file_extension}"
        new_file_path = f'{downloads_path}\{file}'
        os.rename(file_path, new_file_path)
        file_path = new_file_path
        num = num + 1

    # Mova arquivo/pasta pra pasta determinada
    shutil.move(f'{file_path}', f'{folder}')
    