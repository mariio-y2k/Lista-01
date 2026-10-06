codigo_sanduiche = int(input("Digite o código do sanduíche: "))
codigo_bebida = int(input("Digite o código da bebida: "))

if codigo_sanduiche == 100:
    preco_sanduiche = 11.20
elif codigo_sanduiche == 101:
    preco_sanduiche = 8.30
elif codigo_sanduiche == 102:
    preco_sanduiche = 11.50
elif codigo_sanduiche == 103:
    preco_sanduiche = 16.20

if codigo_bebida == 201:
    preco_bebida = 6.00
elif codigo_bebida == 202:
    preco_bebida = 7.50
elif codigo_bebida == 203:
    preco_bebida = 4.70

total = preco_sanduiche + preco_bebida

print(f"Valor a pagar: R$ {total:.2f}")
