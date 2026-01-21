'''
1 - Crie uma função que calcule a gorjeta a ser deixada em um restaurante, baseada no valor total da conta e na porcentagem de
gorjeta desejada. Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.
Parâmetros:
a - valor_conta (float): O valor total da conta
b - porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 10 para 10%)
c - retorna: float: O valor da gorjeta calculada
'''

print("--- Calculadora de Gorjeta ---")

try:
    valor_conta = float(input("Digite o valor total da conta (R$): "))
    porcentagem_gorjeta = float(input("Digite a porcentagem da gorjeta (ex: 10, 15, 20): "))
    
    valor_da_gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    
    valor_total_com_gorjeta = valor_conta + valor_da_gorjeta
    
    print("\n--- Resumo do Pagamento ---")
    print(f"Subtotal: R$ {valor_conta:.2f}")
    print(f"Gorjeta ({porcentagem_gorjeta}%): R$ {valor_da_gorjeta:.2f}")
    print(f"Total a pagar: R$ {valor_total_com_gorjeta:.2f}")
    
except ValueError:
    print("Erro: Por favor, insira apenas números válidos (use ponto para decimais).")