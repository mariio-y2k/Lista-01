tipo = input("Digite o tipo de carne (File Duplo, Alcatra ou Picanha): ")
quantidade = float(input("Digite a quantidade de carne em kg: "))
pagamento = input("A compra será feita com o cartão Tabajara? (S/N): ")

if tipo == "file duplo":
    if quantidade <= 5:
        preco = 34.90
    else:
        preco = 35.80

elif tipo == "alcatra":
    if quantidade <= 5:
        preco = 44.90
    else:
        preco = 46.80

elif tipo == "picanha":
    if quantidade <= 5:
        preco = 66.90
    else:
        preco = 67.80

else:
    print("Tipo de carne inválido.")
    preco = 0

total = quantidade * preco

if pagamento == "S":
    desconto = total * 5 / 100
else:
    desconto = 0

valor_pagar = total - desconto

print("\nCUPOM FISCAL")
print(f"Tipo de carne: {tipo.title()}")
print(f"Quantidade: {quantidade:.2f} kg")
print(f"Preço total: R$ {total:.2f}")

if pagamento == "S":
    print("Tipo de pagamento: Cartão Tabajara")
else:
    print("Tipo de pagamento: Outro")

print(f"Valor do desconto: R$ {desconto:.2f}")
print(f"Valor a pagar: R$ {valor_pagar:.2f}")
