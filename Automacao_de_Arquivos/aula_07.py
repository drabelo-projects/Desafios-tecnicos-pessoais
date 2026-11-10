import os

conteudo_pasta = os.listdir()

for item in conteudo_pasta:
    if os.path.isfile(item):
        print(f"É um arquivo {item}")
    else:
        print(f"{item} não é um arquivo ")   
