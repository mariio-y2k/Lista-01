preco_aquisicao = float(input("Digite o preço de aquisição: R$ "))
preco_aquisicao = float(input("Digite o preço de aquisição: R$ "))

if preco_aquisicao < 50:
    preco_venda = preco_aquisicao + (preco_aquisicao * 45 / 100)
else:
    preco_venda = preco_aquisicao + (preco_aquisicao * 30 / 100)

print(f"Valor de venda: R$ {preco_venda:.2f}")
