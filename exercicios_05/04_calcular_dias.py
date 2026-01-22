'''
4 - Crie um programa que calcule a quantos dias um individuo está vivo de acordo com a data do dia.
'''
from datetime import date


print("--- Calculadora de Dias de Vida ---")

try:
    dia = int(input("Digite o dia do seu nascimento (DD): "))
    mes = int(input("Digite o mês do seu nascimento (MM): "))
    ano = int(input("Digite o ano do seu nascimento (AAAA): "))

    data_nascimento = date(ano, mes, dia)
    hoje = date.today()

    diferenca = hoje - data_nascimento

    if diferenca.days < 0:
        print("\nVocê inseriu uma data no futuro.")
    else:
        print(f"\nVoce está vivo há {diferenca.days:,} dias!".replace(',', '.'))
except ValueError:
    print("\nErro: Por favor, insira números válidos para a data.")