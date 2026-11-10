import os

verificar_arquivo = "aula_01.py"

if os.path.isfile(verificar_arquivo):
    print("Encontramos, definitivamente é arquivo!!! :")
else:
    print("Não encontramos, então não é um arquivo :( :")

