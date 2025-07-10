menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """


saldo = 0
limite_saque = 500
extrato = []  
saques_realizados = 0
LIMITE_SAQUES_DIARIOS = 3

while True:
    opcao = input(menu).strip().lower()  

    
    if opcao == "d":
        try:
            valor = float(input("Informe o valor do depósito: ").strip())
            if valor <= 0:
                print("\033[31mErro: O valor do depósito deve ser positivo.\033[m")
            else:
                saldo += valor
                extrato.append(f"Depósito: R$ {valor:.2f}")
                print(f"\033[32mDepósito de R$ {valor:.2f} realizado com sucesso.\033[m")
        
        except ValueError:
            print("\033[31mErro: Valor inválido. Use apenas números.\033[m")

    
    elif opcao == "s":
        try:
            valor = float(input("Informe o valor do saque: ").strip())
            
            
            erros = []
            if valor <= 0:
                erros.append("O valor deve ser positivo")
            if valor > saldo:
                erros.append("Saldo insuficiente")
            if valor > limite_saque:
                erros.append(f"Valor excede o limite de R$ {limite_saque:.2f}")
            if saques_realizados >= LIMITE_SAQUES_DIARIOS:
                erros.append(f"Limite de {LIMITE_SAQUES_DIARIOS} saques diários atingido")

            if erros:
                print("\033[31mErro no saque:\033[m " + ", ".join(erros) + ".")
            else:
                saldo -= valor
                extrato.append(f"Saque: R$ {valor:.2f}")
                saques_realizados += 1
                print(f"\033[32mSaque de R$ {valor:.2f} realizado com sucesso.\033[m")

        except ValueError:
            print("\033[31mErro: Valor inválido. Use apenas números.\033[m")

    
    elif opcao == "e":
        print("\n" + "=" * 48)
        print("EXTRATO".center(48))
        print("=" * 48)
        
        if not extrato:
            print("Nenhuma movimentação registrada.")
        else:
            print("\n".join(extrato))
        
        print("\n" + "-" * 48)
        print(f"SALDO ATUAL: R$ {saldo:.2f}".rjust(48))
        print("=" * 48)

    
    elif opcao == "q":
        print("Obrigado por usar nosso sistema!")
        break

    
    else:
        print("\033[31mOpção inválida! Digite 'd', 's', 'e' ou 'q'.\033[m")
