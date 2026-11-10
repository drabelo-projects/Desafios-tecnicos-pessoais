import os

pasta = "relatorios"
subpasta = "financeiro"
arquivo = "vendas.xlsx"


juntapastas = os.path.join(pasta,subpasta,arquivo)

print(juntapastas)

