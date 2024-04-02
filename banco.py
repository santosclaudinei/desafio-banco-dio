LIMITE_SAQUE = 2
saldo = 0
LIMITE_VALOR = 500
saques = 0
extrato = ""

while True:

  print("""Menu:
  1. Depositar
  2. Sacar
  3. Extrato
  0. Sair
  """)

  opcao = input("\nEscolha uma opção: ")

  if opcao == "1":
      valor_deposito = float(input("Informe o valor a depositar: "))
      if valor_deposito > 0:
        saldo += valor_deposito
        print(f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso.\n")
        extrato += f"Depósito de R$ {valor_deposito:.2f}"
      else:
          print("Ocorreu um erro na operação. Valor informado para deposito é inválido.")
  elif opcao == "2":
      if(saques <= LIMITE_SAQUE):
          valor_saque = float(input("Informe o valor a sacar: "))
          if(valor_saque < LIMITE_VALOR):
            if(saldo - valor_saque < 0):
              print("Ocorreu um erro na operação. Saldo insufisciente.")
            else:
              saldo -= valor_saque
              print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso.\n")
              extrato += f"\nSaque de R$ {valor_saque:.2f}\n"

              saques += 1
          else:
              print("Desculpe! O limite de valor para saques diários foi ultrapassado.")
      else:
          print("Desculpe! O limite de saques diários foi atingido. \n")
  elif opcao == "3":
      caractere = "="
      print(f"\n{10*caractere} EXTRATO {10*caractere}")
      print(extrato)
      print(f"\nSaldo => R$ {saldo:.2f}")
      print(f"{29*caractere}")
  else:
    print("Obrigado por usar o nosso banco.")
    break