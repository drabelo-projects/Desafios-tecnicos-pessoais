import os

pasta = "relatorios"

if os.path.exists(pasta):
    print("A pasta existe!")
else:
    print("A pasta não existe!")