frangos = int(input("Digite a quantidade de frangos: "))

anel_chip = 4.00
anel_alimento = 3.50

gasto_por_frango = anel_chip + (anel_alimento * 2)
gasto_total = frangos * gasto_por_frango

print(f"Gasto total: R$ {gasto_total:.2f}")
