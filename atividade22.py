preco = float(input("Digite o preço do produto: R$ "))

desconto = preco * 10 / 100
novo_preco = preco - desconto

print(f"Novo preço: R$ {novo_preco:.2f}")

