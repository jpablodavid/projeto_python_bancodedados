import textwrap

def menu():
  menu = """\n
  ####################### MENU ################# 
  [d]\tDepositar
  [s]\tSacar
  [e]\tExtrato
  [nc]\tNova Conta
  [lc]\tListar Contas
  [nu]\tNovo Usuario
  [q]\tSair
  => """
  return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
  if valor > 0:
    extrato += f' Deposito:\tR$ {valor:.2f}\n'
    saldo += valor
    print(f'\nDeposito no valor de R$ {valor:.2f} confirmado')
  else:
    print('\nSó são aceito valores positivos')

  return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if saldo < valor:
      print(f'\nNão foi possivel efetuar o saque no valor R$ {valor:.2f}, seu saldo atual é de R$ {saldo:.2f}')
    elif numero_saques >= LIMITE_SAQUES:
      print(f'\nNão foi possivel efetuar o saque no valor R$ {valor:.2f}, numero de saques passou o limite de {LIMITE_SAQUES} saques diarios')
    elif valor > VALOR_MAXIMO_SAQUE:
      print(f'\nNão foi possivel efetuar o saque no valor R$ {valor:.2f}, Valor de saque passou o limite de R$ {VALOR_MAXIMO_SAQUE:.2f} por saque')
    elif valor > 0:
      extrato += (f"Saque\t\tR$ {valor:.2f} \n")
      saldo -= valor
      numero_saques += 1
      print(f"\nSaque no valor de R$ {valor:.2f} confirmado")
    else:
      print("\nValor informado é invalido")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
  print("\n############ EXTRATO #############")
  print("Não foram executadas movimentações." if not extrato else extrato)
  print(f"\nSaldo:\t\tR$ {saldo:.2f}")
  print('####################################')

def criar_usuario(usuarios):
  cpf = input("Informe seu CPF (somente número): ")
  usuario = filtrar_usuario(cpf, usuarios)

  if usuario:
    print("\nJá existe um usuário com esse CPF: ")
    return
  
  nome = input("Digite seu nome completo: ")
  data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
  endereco = input("Informe seu Endereco (Logradouro, número - bairro - cidade/sigla estado): ")

  usuarios.append({'nome': nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

  print(" Usuário cadastrado com sucesso!")

def filtrar_usuario(cpf, usuarios):
  usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
  return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
  cpf = input("Informe o CPF do Usuário: ")
  usuario = filtrar_usuario(cpf, usuarios)

  if usuario:
    print("\nConta criada com sucesso!")
    return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

  print("\nUsuário não encontrado")

def listar_contas(contas):
  for conta in contas:
    linha = f"""\
      agência:\t{conta["agencia"]}
      C/C:\t\t{conta["numero_conta"]}
      Titula:\t{conta["usuario"]["nome"]}
    """
    print("*" * 100)
    print(textwrap.dedent(linha))

def main():
  AGENCIA = "0001"
  LIMITE_SAQUES = 3
  VALOR_MAXIMO_SAQUE = 500  

  saldo = 0
  limite = 0
  extrato = ''
  numero_saques = 0
  usuarios = []
  contas = []
  numero_conta = 1
  
  while True:

    opcao = menu()

    if opcao == 'd':
      valor = float(input('Valor do Deposito: '))

      saldo, extrato = depositar(saldo, valor, extrato)
        
    elif opcao == 's':
      valor = float(input('Valor do Saque: '))

      saldo, extrato = sacar(
        saldo=saldo,
        valor=valor,
        extrato=extrato,
        limite=limite,
        numero_saques=numero_saques,
        limite_saques=LIMIT_SAQUES,
      )

    elif opcao == 'e':
      exibir_extrato(saldo, extrato=extrato)

    elif opcao == 'nu':
      criar_usuario(usuarios)

    elif opcao == 'nc':
      conta = criar_conta(AGENCIA, numero_conta, usuarios)

      if conta:
        contas.append(conta)
        numero_conta += 1

    elif opcao == 'lc':
      listar_contas(contas)

    elif opcao == 'q':
      break

    else: 
      print('Operação inválida, por favor selecione novamente a operação desejada.')

main()
