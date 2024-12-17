from time import sleep

extrato = ""
name = ""
saldo = 0
limite = 500
limite_saque = 3
numero_saques=0
fins= "Não declarado."
print("Bem-vindo!!!\nBanco Borges Finance\nEstamos à sua disposição.")
while True:
    print("""Escolha uma opção:
    [1] Transferência
    [2] Depósito
    [3] Saque
    [4] Extrato
    [0] Sair""")
    
    op = int(input("Qual opção você deseja:"))
    
    #Transferência
    if op == 1:
        while True:
            deposito = int(input("Valor da transferência: R$ "))
            forma = str(input("[] PIX\n[] TED\n[] DOC\nQual a forma de transferência? ")).upper().strip()
            if forma == "PIX":
                name = str(input("Digite o nome: "))
                pix = input("Digite a chave PIX: ")
            elif forma == "TED":
                name = str(input("Digite o nome: "))
                ag = input("Digite a agência: ")
                cc = input("Digite a Conta Corrente: ")
                cpf = int(input("Digite o CPF: "))
            elif forma == "DOC":
                name = str(input("Digite o nome: "))
                ag = input("Digite a agência: ")
                cc = input("Digite a Conta Corrente: ")
                cpf = int(input("Digite o CPF: "))
            else:
                print("Opção inválida!!")
            
            extrato = extrato + "Transferência de R${:.2f} via {} para {}\n".format(deposito, forma, name)
            print("Transferência realizada com sucesso.")
            sleep(1)
            tenta = str(input("Deseja transferir mais algum valor? [S/N]")).upper().strip()[0]
            if tenta == "N":
                print("Obrigado! Volte sempre.")
                break
            elif tenta == "S":
                print("Digite novamente.")
            else:
                print("Opção inválida!!!")
                print("Tente de novo!!!")
    
    #depósito
    elif op == 2:
    
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo = saldo + valor
            extrato += f"Depósito de R$ {valor:.2f}\n"

    #saque       
    elif op == 3:
        
             
        while True:
            if 0>= saldo <=10:
                print("Tente outra opção!\n Limite para saque é de R$10.00")
                break
            print("Você está com saldo de R${}".format(saldo))
            
            valor = float(input("Informe o valor do saque: "))

            excedeu_saldo = valor > saldo

            excedeu_limite = valor > limite

            excedeu_saques = numero_saques >= limite_saque

            if excedeu_saldo:
                print("Operação falhou! Você não tem saldo suficiente.")

            elif excedeu_limite:
                print("Operação falhou! O valor do saque excede o limite.")

            elif excedeu_saques:
                print("Operação falhou! Número máximo de saques excedido.")

            elif valor > 0:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f} para {fins}\n"
                numero_saques = numero_saques + 1

            else:
                print("Operação falhou! O valor informado é inválido.")

            tenta = str(input("Deseja realizar mais um saque: [SIM/NÃO]")).upper().strip()[0]
            if tenta == "S":
                    print("Digite Novamente")
                    fins=str(input("Para onde será destinado o valor?"))
            elif tenta == "N":
                    break
            else:
                    print("Opção Ínvalida!! Tente de novo.")

    
    #extrato
    elif op == 4:
        print("Essas são as transações feitas:\n{}".format(extrato))
    
    #sair        
    elif op == 0:
        print("Encerrado... Volte sempre!!")
        break
