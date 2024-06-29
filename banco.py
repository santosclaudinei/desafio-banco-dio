import textwrap


def exibir_menu():
    print("Menu:")
    print("1. Depositar")
    print("2. Sacar")
    print("3. Extrato")
    print("4. Criar Usuário")
    print("5. Criar Conta")
    print("6. Listar Contas")
    print("0. Sair")


def depositar(deposito, saldo, extrato):
    if deposito > 0:
        saldo += deposito
        print(f"Depósito de R$ {deposito:.2f} realizado com sucesso.\n")
        extrato += f"Depósito de R$ {deposito:.2f}"
        return saldo, extrato
    else:
        print("Ocorreu um erro na operação. Valor informado para deposito é inválido.")


def sacar(saldo, valor_saque, extrato, LIMITE_VALOR, LIMITE_SAQUES, numero_saques):
    operacao = validacoes_saque(saldo, valor_saque, extrato, numero_saques, LIMITE_SAQUES, LIMITE_VALOR)
    if operacao:
        saldo -= valor_saque
        numero_saques += 1
        print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso.\n")
        extrato += f"\nSaque de R$ {valor_saque:.2f}\n"
    return saldo, extrato, numero_saques



def validacoes_saque(saldo, valor_saque, extrato, numero_saques, LIMITE_SAQUES, LIMITE_VALOR):
    if saldo < valor_saque:
        print("Ocorreu um erro na operação. Saldo insufisciente.")
        return False
    elif numero_saques >= LIMITE_SAQUES:
        print("Desculpe! O limite de valor para saques diários foi ultrapassado.")
        return False
    elif valor_saque > LIMITE_VALOR:
        print("Desculpe! O limite de saques diários foi atingido. \n")
        return False
    elif valor_saque <= 0:
        print("Ocorreu um erro durante a execução do programa. Valor de saque inválido.")
        return False
    return True


def exibir_extrato(extrato, saldo):
    caractere = "="
    print(f"\n{10*caractere} EXTRATO {10*caractere}")
    print(extrato)
    print(f"\nSaldo => R$ {saldo:.2f}")
    print(f"{29*caractere}")


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = pesquisa_usuario(cpf, usuarios)

    if usuario:
        print(f"O usuário com o cpf: {cpf} já possuí cadastro")

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento: ")
    endereco = input("Informe o endereço: ")

    usuarios.append({"nome": nome, "data_nacimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    caractere = "="
    print(f"\n{10*caractere} Usuário cadastrado com sucesso. {10*caractere}")


def pesquisa_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = pesquisa_usuario(cpf, usuarios)
    caractere = "="

    if usuario:
        print(f"\n{10*caractere} Conta criada com sucesso. {10*caractere}\n")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print(f"\n{10*caractere} Não foi possível localizar usuário com CPF: {cpf} Conta não encontrada.\n{10*caractere}")


def listar_contas(contas):
    caractere = "="
    print(f"\n{10*caractere} Contas {10*caractere}\n")
    for conta in contas:
        dados_conta = f"""\
            Agência:\t {conta['agencia']}
            Conta Corrente:\t {conta['numero_conta']}
            Titular:\t {conta['usuario']['nome']}
        """
        print(textwrap.dedent(dados_conta))
    print(f"{28*caractere}\n")


def sair():
    print("Obrigado por usar o nosso banco.")
    return False


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    LIMITE_VALOR = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        exibir_menu()
        opcao = input("\nEscolha uma opção: ")

        match opcao:
            case "1":
                valor_deposito = float(input("Informe o valor a depositar: "))
                saldo, extrato = depositar(valor_deposito, saldo, extrato)
            case "2":
                valor_saque = float(input("Informe o valor a sacar: "))
                saldo, extrato, numero_saques = sacar(saldo, valor_saque, extrato, LIMITE_VALOR, LIMITE_SAQUES, numero_saques)
            case "3":
                exibir_extrato(extrato, saldo)
            case "4":
                criar_usuario(usuarios)
            case "5":
                numero_conta = len(contas) + 1
                conta = criar_conta(AGENCIA, numero_conta, usuarios)

                if conta:
                    contas.append(conta)
            case "6":
                listar_contas(contas)
            case "0":
                sair()
                break
            case _:
                print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()