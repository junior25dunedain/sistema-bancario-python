
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""
extrato = ""
saldo = 0
numero_saques = 0
limite = 500
LIMITE_SAQUES = 3

while True:
    op = input(menu)

    if op == 'd':
        valor = float(input('Informe o valor do depósito: '))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print('Operação falhou! valor inválido.')

    elif op == 's':
        valor = float(input('Informe o valor do saque: '))
        if valor > saldo:
            print('Operação falhou! Você não tem saldo suficiente.')
        elif valor > limite:
            print('Operação falhou! valor excedeu o limite diário.')
        elif numero_saques >= LIMITE_SAQUES:
            print('Operação falhou! numero de saques foi excedido.')
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print('Operação falhou! valor inválido.')

    elif op == 'e':
        print('\n*************** EXTRATO ********************')
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print('**********************************************')
    elif op == 'q':
        break

    else:
        print('Operação inválida, por favor selecione uma operação válida!!!')

