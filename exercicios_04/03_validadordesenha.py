'''
3 - Criar um código que serve para verificar se uma senha digitada pelo usuário atende a critérios básicos de segurança.

a - deve ter pelo menos 8 caracteres.
b - deve conter pelo menos um número.
'''

def verificar_senha():
    print("--- Validador de Senha Segura ---")
    senha = input("Digite a sua senha: ")

    # Critério 1: Pelo menos 8 caracteres
    tamanho_valido = len(senha) >= 8

    # Critério 2: Conter pelo menos um número
    tem_numero = False
    for caractere in senha:
        if caractere.isdigit():
            tem_numero = True
            break

    if tamanho_valido and tem_numero:
        print("\n✅ Senha aprovada! Ela atende aos critérios de segurança.")
    else:
        print("\n❌ Senha reprovada.")
        if not tamanho_valido:
            print("- A senha deve ter no mínimo 8 caracteres.")
        if not tem_numero:
            print("- A senha deve conter pelo menos um número.")

verificar_senha()