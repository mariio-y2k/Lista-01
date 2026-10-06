litros = float(input("Digite a quantidade de litros: "))
combustivel = input("Digite o tipo de combustível (A-Álcool / G-Gasolina): ").upper()

if combustivel == "A":
    preco = 1.90

    if litros <= 20:
        desconto = 3
    else:
        desconto = 5

elif combustivel == "G":
    preco = 2.50

    if litros <= 20:
        desconto = 4
    else:
        desconto = 6

else:
    print("Tipo de combustível inválido.")
    preco = 0
    desconto = 0

valor = litros * preco
valor_desconto = valor * desconto / 100
valor_pagar = valor - valor_desconto

if preco > 0:
    print(f"Valor sem desconto: R$ {valor:.2f}")
    print(f"Desconto: {desconto}%")
    print(f"Valor a pagar: R$ {valor_pagar:.2f}")
