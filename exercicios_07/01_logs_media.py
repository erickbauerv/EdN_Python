'''
1 - Crie um programa que lê um arquivo CSV de logs de treinamento com a biblioteca pandas, calcule e 
exiba a média e o desvio padrão da coluna tempo_execucao, caso e o arquivo não exista ou houver 
erro na leitura, mostre uma mnesagem de erro.
'''

import pandas as pd
import os

def analisar_logs(nome_arquivo):
    try:
        # Verifica se o arquivo existe antes de tentar abrir
        if not os.path.exists(nome_arquivo):
            raise FileNotFoundError(f"O arquivo '{nome_arquivo}' não foi encontrado.")
        
        # Lê o arquivo CSV
        df = pd.read_csv(nome_arquivo)

        # Verifica se a coluna necessário existe
        if 'tempo_execucao' not in df.columns:
            print(f"Erro: A coluna 'tempo_execucao' não existe no arquivo.")
            return
        
        # Calcula as métricas
        media = df['tempo_execucao'].mean()
        desvio_padrao = df['tempo_execucao'].std()
        
        # Exibe os resultado formatados
        print("-" * 30)
        print(f"Análise de Logs: {nome_arquivo}")
        print("-" * 30)
        print(f"Média de tempo: {media:2f}s")
        print(f"Desvio padrão: {desvio_padrao:.2f}s")
        print("-" * 30)
    except FileNotFoundError as e:
        print(f"Erro de arquivo: {e}")
    except pd.errors.EmptyDataError:
        print("Erro: O arquivo CSV está vazio.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

analisar_logs('treinamento_logs.csv')
