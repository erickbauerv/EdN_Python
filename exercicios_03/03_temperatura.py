'''
3- Conversor de Temperatura
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin.
O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.
'''

temperatura = float(input("Digite a temperatura: "))
unidadeorigem = input("Digite a unidade de medida de origem, (C) Celsius, (F) Fahrenheit e (K) Kelvin: ").upper()
unidadedestino = input("Digite a unidade de medida de destino, (C) Celsius, (F) Fahrenheit e (K) Kelvin: ").upper()

if unidadeorigem == "C" and unidadedestino =="F":
    resultado = (temperatura * 9/5) + 32
elif unidadeorigem == "C" and unidadedestino == "K":
    resultado = temperatura + 273.15
elif unidadeorigem == "F" and unidadedestino =="C":
    resultado = (temperatura - 32) * 5/9
elif unidadeorigem == "F" and unidadedestino == "K":
    resultado = (temperatura - 32) * 5/9 + 273.15
elif unidadeorigem == "K" and unidadedestino =="C":
    resultado = temperatura - 273.15
elif unidadeorigem == "K" and unidadedestino == "F":
    resultado = (temperatura - 273.15) * 9/5 + 32
else:
    resultado = temperatura

print(f"Temperatura: {round(resultado, 2), unidadedestino}")