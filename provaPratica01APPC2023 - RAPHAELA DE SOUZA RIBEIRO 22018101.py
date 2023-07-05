#NOME: RAPHAELA DE SOUZA RIBEIRO
#RA: 22018101
print("Bem vindo ao sistema de caixa de mercado!\n")
print("Vamos começar inserindo a senha para abrir o caixa.\n")
#senha: 123456
senha = 0
saldoINICIAL = -1.00
while senha != 123456:
    try:
        senha = int(input("Por favor, digite sua senha: "))
        if senha == 123456:
            print("\nCaixa aberto!\n")
        else:
            print("Senha incorreta! Tente novamente...")
    except (ValueError, TypeError):
        print("Senha incorreta! Tente novamente...")
while saldoINICIAL == -1.00:
    try:
        saldoINICIAL = float(input("Por favor, insira o saldo inicial: "))
        if saldoINICIAL >= 0.00:
            print("\nSaldo registrado!")
            print(f"\nSaldo atual: R${saldoINICIAL:.2f}")
        else:
            print("Valor inválido. Tente novamente...")
    except (ValueError, TypeError):
        print("Valor inválido. Tente novamente...")
print("\nEscolha uma opção: \n")
print("[1] Consultar saldo inicial;")
print("[2] Registrar uma venda;")
print("[3] Fechar o caixa.")
nomeProduto = ' '
valorProduto = 0.00
qtdProduto = 0
valorVenda = 0
troco = 0.00
numVendas = 0
itensVendidos = 0
somaValoresVendas = 0
lucro = 0.00
opcaoEscolhida = 0
respostaNovoItem = ' '
while opcaoEscolhida != 3:
    opcaoEscolhida = int(input("Digite o número da opção escolhida: "))
    if opcaoEscolhida == 1:
        print(f"Consultando saldo atual...\nSeu saldo é de R${saldoINICIAL:.2f}")
        break
    if opcaoEscolhida == 2:
        while True:
            while True:
                try:

                    nomeProduto = input("\nDigite o nome do produto: ")
                    if nomeProduto.isalpha():
                        print("\nNome válido!")
                        break
                    else:
                        print("\nNome inválido! Tente novamente...")
                except (ValueError, TypeError):
                    print("\nNome inválido! Tente novamente...")
            while True:
                try:
                    valorProduto = float(input(f"\nQual o valor de {nomeProduto}? "))
                    if valorProduto > 0.00:
                        print("\nValor registrado!")
                        print(f"\nValor unitário: R${valorProduto:.2f}")
                        break
                    else:
                        print("\nValor inválido. Tente novamente...")
                except (ValueError, TypeError):
                    print("\nValor inválido. Tente novamente...")
            while True:
                try:
                    qtdProduto = int(input(f"\nPor favor, a quantidade de {nomeProduto}: "))
                    if qtdProduto > 0:
                        print("Produto(s) registrado(s)!\n")
                        break
                    else:
                        print("\nValor inválido. Tente novamente...")
                except (ValueError, TypeError):
                    print("\nValor inválido. Tente novamente...")
            valorVenda = valorVenda + (valorProduto * qtdProduto)
            numVendas = numVendas + 1
            itensVendidos = itensVendidos + qtdProduto
            while True:
                while respostaNovoItem: #validar string vazia
                    respostaNovoItem = input("\n\nDeseja registrar outro item nesta venda? (S/N): ")
                    if respostaNovoItem.upper() != "S" and respostaNovoItem.upper() != "N":
                        respostaNovoItem = input("\nOpção inválida. Digite S para registrar outro item ou N para finalizar: ")
                    else:
                        if respostaNovoItem.upper() == "N":
                            troco = saldoINICIAL-valorVenda
                            if troco >= 0:
                                print(f"\nTroco: R${troco:.2f}")
                                break
                            else:
                                print("\nPagamento recusado.")
                                break
                    if respostaNovoItem.upper() == "S":
                        break
                if respostaNovoItem.upper() == "S":
                    break
                respostaNovaVenda = input("\n\nDeseja registrar uma nova venda? (S/N): ")
                while respostaNovoItem.upper() == "N": #validar string vazia
                    if respostaNovaVenda.upper() != "S" and respostaNovaVenda.upper() != "N":
                        respostaNovaVenda = input("\nOpção inválida. Digite S para registrar outro item ou N para finalizar: ")
                    if respostaNovaVenda.upper() == "N":
                        somaValoresVendas = somaValoresVendas + valorVenda
                        saldoFINAL = troco
                        lucro = somaValoresVendas
                        print(f"\n\nQuantidade de vendas realizadas: {numVendas}")
                        print(f"Quantidade de itens vendidos: {itensVendidos}")
                        print(f"Valor total das vendas: R${somaValoresVendas:.2f}")
                        print(f"Saldo inicial: R${saldoINICIAL:.2f}")
                        print(f"Lucro bruto: {lucro:.2f}")
                        print("\nVENDA(S) FINALIZADA(S)!\n")
                        break
                    break
                if respostaNovaVenda.upper() != "S":
                    quit()
                else:
                    break
    if opcaoEscolhida == 3:
        print("Caixa fechado.")
        break