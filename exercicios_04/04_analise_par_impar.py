'''
4 - Criar um código que serve para analisar números digitados pelo usuário, classificando-os como pares ou ímpares e contabilizando quantos de cada tipo foram inseridos.
'''

def analisador_de_numeros():
    print("--- Analisador de Números (Par ou Ímpar) ---")
    print("Digite 'sair' para encerrar e ver os resultados.\n")

    pares = 0
    impares = 0

    while True:
        entrada = input("Digite um número inteiro: ").strip().lower()

        if entrada == 'sair':
            break

        try:
            numero = int(entrada)

            if numero % 2 == 0:
                print(f"O número {numero} é PAR.")
                pares += 1
            else:
                print(f"O número {numero} é ÍMPAR.")
                impares += 1
        
        except ValueError:
            print("Entrada inválida! Por favor, digite um número inteiro ou 'sair'.")

    print("\n--- Resumo dos Resultados ---")
    print(f"Total de números pares: {pares}")
    print(f"Total de números ímpares: {impares}")
    print(f"Total de números digitados: {pares + impares}")
    print("Programa encerrado.")

analisador_de_numeros()