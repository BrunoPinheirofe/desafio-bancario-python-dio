menu = """
[d] - Depositar
[s] - Sacar
[e] - Extrato
[q] - Sair

=> """

saldo = 0
limite = 500
numero_saques = 0
extrato = ""
LIMITE_SAQUES = 3

while True:
    opcao = input(menu).lower()
    if opcao == "d":
        valor_deposito = float(
            input("Digite o valor que deseja adicionar na sua conta R$: ")
        )
        if valor_deposito > 0:
            saldo += valor_deposito
            print(
                f"valor do deposito de {valor_deposito:.2f} foi adicionado com sucesso"
            )
            extrato += f"deposito de:       {valor_deposito:.2f}\n"

    elif opcao == "s":
        valor_saque = float(input("Digite o valor que deseja sacar de sua conta R$: "))
        if valor_saque > saldo:
            print("Operação falhou!!! Valor de deposito exedeu o saldo")
        elif valor_saque > limite:
            print("Operação falhou!!! Valor de deposito exedeu o limite")
        elif numero_saques > LIMITE_SAQUES:
            print("Operação falhou!!! O numero maximo de saques por dia foi exedido")
        elif valor_saque > 0:
            saldo -= valor_saque
            extrato += f"saque de:       {valor_saque:.2f}\n"
            numero_saques += 1
            print(f"Saque de {valor_saque:.2f} realizado com sucesso!")
        else:
            print("Valor informado para deposito não é considerado valido")
    elif opcao == "e":
        print("EXTRATO".center(50, "="))
        print("Nenhuma transição executada" if not extrato else extrato)
        print("=" * 50)
    elif opcao == "q":
        print("SAINDO...")
        break
    else:
        print("Opção invalida".upper())
