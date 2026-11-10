import os

pasta = "relatorios"
arquivo = "vendas.xlsx"

juntapastas = os.path.join(pasta, arquivo)

print("Diretório atual:", os.getcwd())
print(juntapastas)
print(os.listdir(pasta))

if os.path.isfile(juntapastas):
    
    print(f"O arquivo {arquivo} está dentro de relatorios!")
else:
    print(f"O arquivo {arquivo} não está dentro de relatorios!")