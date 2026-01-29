'''
04 - Crie um progrma que leia e escreva arquivos no formato JSON, que salve em um dicionário 
com nome, idade e cidade em um arquivo JSON e depois leia o mesmo arquivo exibindo os dados, caso
o arquivo não existir ou ocorrer erro ao salvar, mostre uma mensagem de erro.
'''

import json
import os

def gerenciar_json():
    nome_arquivo = 'dados_usuario.json'

    # 1. Coleta de dados
    dados = {
        "nome": input("Digite o nome: "),
        "idade": input("Digite a idade: "),
        "cidade": input("Digite a cidade: ")
    }

    # 2. Escrita do arquivo (Salvar)
    try:
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)
        print(f"\n Dados salvos com sucesso em '{nome_arquivo}'!")
    except Exception as e:
        print(f"\n Erro ao salvar o arquivo: {e}")
        return
    
    print("-" * 30)

    # 3. Leitura do arqquivo (Exibir)
    try:
        if os.path.exists(nome_arquivo):
            with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
                dados_carregados = json.load(arquivo)

            print("Lendo dados do arquivo:")
            for chave, valor in dados_carregados.items():
                print(f"{chave.capitalize()}: {valor}")
        else:
            print("O arquivo não foi encontrando para leitura.")
    except json.JSONDecodeError:
        print("Erro: O arquivo existe, mas o formato JSON está corrompido.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado na leitura: {e}")

gerenciar_json()