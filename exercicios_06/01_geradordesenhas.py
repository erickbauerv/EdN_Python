'''
1 - Crie um programa que gere senhas aleatórias com letras, números e símbolos e que 
o usuário também escolha o tamanho da senha para criar senhas seguras automaticamente.
'''

import random
import string

print("--- Gerador de Senhas Seguro ---")
    
try:
    tamanho = int(input("Digite o comprimento desejado para a senha: "))
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for i in range(tamanho))
    
    print(f"\nSua senha gerada é: {senha}")
    
except ValueError:
    print("Erro: Por favor, digite apenas números inteiros para o tamanho.")