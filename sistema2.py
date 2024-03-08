import textwrap

def Menu():
    menu = """\n
    ______________________Menu______________________
                    [d] Depositar
                    [s] Sacar
                    [e] Extrato
                    [q] Sair
                    [nc] Nova conta
                    [lc] Listar contas
                    [nu] Novo usuário
    ------------------------------------------------
    ->
    """
    return input(textwrap.dedent(menu))

extrato = ""
saldo = 0
numero_saques = 0
limite = 500
LIMITE_SAQUES = 3
AGENCIA = '0001'
contas = []
usuarios = []

def Deposito(saldo,extrato,/):
     valor = float(input('Informe o valor do depósito: '))
     if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print('Depósito realizado com sucesso!')
     else:
            print('Operação falhou! valor inválido.')
     return saldo, extrato

def Sacar(*,saldo,extrato,limite,numero_saques,limite_saques):
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
            print('Saque realizado com sucesso!')
    else:
            print('Operação falhou! valor inválido.')
    return saldo, extrato

def Extrato(saldo,/,*,extrato):
    print('\n*************** EXTRATO ********************')
    print('Não foram realizadas movimentações.' if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print('**********************************************')

def Cadastra_usuario(usuarios):
    cpf = input('Informe o CPF (somente número): ')
    if usuarios:
        for i in usuarios:
            if i['cpf'] == cpf:
                print('Já existe usuário com esse CPF!')
                return
    nome = input('Informe o nome completo: ')
    data_nascimento = input('Informe a data de nascimento (dd-mm-aaaa): ')
    endereco = input('Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ')
    usuarios.append({'nome':nome,'data_nascimento':data_nascimento,'cpf':cpf,'endereço':endereco})
    print('=== Usuário criado com sucesso! ===')

def Criar_conta(agencia,numero_conta,usuarios): 
    cpf = input('Informe o CPF (somente número): ')
    if usuarios:
        for i in usuarios:
            if i['cpf'] == cpf:
                usuario = i
                print('=== Conta criada com sucesso! ===')
                return {'agencia':agencia, 'numero_conta':numero_conta,'usuario':usuario}
    print('Usuário não encontrado, fluxo de criação de conta encerrado!')
    return None

def Listar_contas(contas):
    for conta in contas:
        linha = f"""
             Agência:\t{conta['agencia']}
             C/C:\t\t{conta['numero_conta']}
             Titular:\t{conta['usuario']['nome']}
        """
        print('='*100)
        print(textwrap.dedent(linha))

while True:
    op = Menu()

    if op == 'd':
       saldo, extrato = Deposito(saldo,extrato)

    elif op == 's':
        saldo, extrato = Sacar(saldo=saldo,extrato=extrato,limite=limite,numero_saques=numero_saques,limite_saques=LIMITE_SAQUES)

    elif op == 'e':
       Extrato(saldo,extrato=extrato)
    elif op == 'q':
        break
    elif op == 'nu':
        Cadastra_usuario(usuarios)
    elif op == 'nc':
        numero_conta = len(contas) + 1
        conta = Criar_conta(AGENCIA, numero_conta, usuarios)
        if conta:
            contas.append(conta)
    elif op == 'lc':
        Listar_contas(contas)
    else:
        print('Operação inválida, por favor selecione uma operação válida!!!')
