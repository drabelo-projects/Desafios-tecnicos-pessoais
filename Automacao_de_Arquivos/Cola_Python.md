# 🐍 Cola Python — Automação de Arquivos

## 1. Biblioteca OS

```python
import os
```
Permite interagir com o sistema operacional.

## 2. Diretórios e arquivos

| Comando | Função |
|---|---|
| `os.getcwd()` | Mostra a pasta atual |
| `os.listdir()` | Lista arquivos e pastas |
| `os.path.exists()` | Verifica se um caminho existe |
| `os.path.isfile()` | Verifica se é um arquivo |
| `os.path.isdir()` | Verifica se é uma pasta |
| `os.path.join` | Juntar pastas e arquivos |

## 3. Estruturas básicas

```python
for item in lista:
    print(item)
```
Percorre os elementos de uma lista.

```python
if condicao:
    print("Verdadeiro")
else:
    print("Falso")
```
Executa uma ação conforme a condição.

## 4. Funções úteis

| Comando | Função |
|---|---|
| `len(lista)` | Conta os elementos |
| `print()` | Exibe informações |
| `input()` | Recebe dados |


# Listar somente arquivos de uma pasta
import os

conteudo_pasta = os.listdir()

for item in conteudo_pasta:
    if os.path.isfile(item):
        print(item)


Comando	Função
os.path.join()	Junta partes de um caminho de arquivo ou pasta

Exemplo:
caminho = os.path.join("relatorios", "vendas.xlsx")