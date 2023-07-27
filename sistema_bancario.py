menu = """ 
[d] Depositar
[s] Sacar
[e] Extratos
[q] Sair

=> """

saldo = 0
limite = 0
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3
VALOR_MAXIMO_SAQUE = 500
  

while True:

  opcao = input(menu)

  if opcao == 'd':
    valor = float(input('Digite o valor do Deposito: '))
    if valor <= 0:
      print('Só são aceito valores positivos')
    else:
      extrato += f' Deposito no Valor de: R$ {valor:.2f} \n'
      saldo += valor
      print(f'Deposito no valor de R$ {valor:.2f} confirmado')
      
  elif opcao == 's':
    valor = float(input('Digite o valor do Saque: '))
    if valor <= 0:
      print('Só são aceito valores positivos')
    else:
      if saldo < valor:
        print(f'Não foi possivel efetuar o saque no valor R$ {valor:.2f}, seu saldo atual é de R$ {saldo:.2f}')
      elif numero_saques >= LIMITE_SAQUES:
        print(f'Não foi possivel efetuar o saque no valor R$ {valor:.2f}, numero de saques passou o limite de {LIMITE_SAQUES} saques diarios')
      elif valor > VALOR_MAXIMO_SAQUE:
        print(f'Não foi possivel efetuar o saque no valor R$ {valor:.2f}, Valor de saque passou o limite de R$ {VALOR_MAXIMO_SAQUE:.2f} por saque')
      else:
        extrato += (f" Saque no Valor de: R$ {valor:.2f} \n")
        saldo -= valor
        numero_saques += 1
        print(f"Deposito no valor de R$ {valor:.2f} confirmado")

  elif opcao == 'e':
    print("############ EXTRATO #############")
    print(" Não foram executadas movimentações." if not extrato else extrato)
    print(f"\n Saldo: R$ {saldo:.2f}")
    print('##################################')

  elif opcao == 'q':
    break

  else: 
    print('Operação inválida, por favor selecione novamente a operação desejada.')
