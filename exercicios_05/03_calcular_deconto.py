'''
3 - Crie um programa que serve para calcular o preço final de um produto após aplicar um desconto percentual.
a - Cálculo de desconto: Calcula o valor do desconto baseado em uma porcentagem.
b - Preço final: Determina o novo preço após o desconto.
c - Formatação: Arredonda o resultado para 2 casas decimais (centavos).
d - Interação com usuário: Pede os valores necessários e mostra o resultado formatado.
'''

print("--- Simulador de Desconto ---")

preco_original = float(input("Digite o preço original do produto: R$ "))
porcentagem_desconto = float(input("Digite a porcentagem de desconto (ex: 15): "))

valor_desconto = preco_original * (porcentagem_desconto / 100)

preco_final = preco_original - valor_desconto

print("-----------------------------------")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Preço final com {porcentagem_desconto}% de desconto: R$ {preco_final:.2f}")