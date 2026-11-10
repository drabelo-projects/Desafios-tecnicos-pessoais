import os

nome_pasta = "documentos"

if os.path.exists(nome_pasta):
    print("Diretório encontrado!! :")
else:
    print("Diretório não encontrado!! : ")    