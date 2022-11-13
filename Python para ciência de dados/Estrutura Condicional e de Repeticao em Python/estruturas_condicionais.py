# IF
profissao = input("Digite se você é cantor ou cozinheiro:")

if profissao == "cantor":
    print("Você pode se inscrever no The Voice!")

if profissao == "cozinheiro":
    print("Você pode se inscrever no Masterchef!")

# IF/ELSE
preco_produto = 100
dinheiro_disponivel = float(input("Digite quanto você tem para comprar o produto: "))

if dinheiro_disponivel >= preco_produto:
    print("Você pode adquirir o produto.")
else: 
    print("Você não tem o suficiente para comprar o produto.")

# ELIF
opcao = int(input("Digite 1 para ver o valor da fatura ou 2 para pagar no débito automático: "))
fatura = 400

if opcao == 1:
    print(f"O valor da sua fatura é {fatura}")
elif opcao == 2:
    print("Sua fatura será paga via débito automático.")
else: 
    print("Opção inválida!")
