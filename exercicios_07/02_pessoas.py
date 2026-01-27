'''
2 - Crie um programa que cria um arquivo com nome, idade e cidade de algumas pessoas, que este
programa escreva os dados em formato tabular e salve no arquivo escolhido pelo usuário, caso
ocorra um erro ao salvar, mostre uma mensagem de falha.
'''

import csv

def criar_csv_pessoas():
    caminho_arquivo = "C:\Users\10\Desktop\TurmasEDN\Exercicios_7\pessoas.csv"
    pessoas = [
        ["Nome", "Idade", "Cidade"],
        ["João", 22, "Porto Alegre"]
        ["Pedro", 20, "São paulo"]
        ["Claudia", 19, "Rio de Janeiro"]
    ]
    try:
        with open(caminho_arquivo, mode="w", newline="", encoding="utf-8") as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerows(pessoas)
        print(f"Arquivo CSV criado em: {caminho_arquivo}")
    except Exception as erro:
        print(f"Falha ao salvar CSV: {caminho_arquivo}")

criar_csv_pessoas()