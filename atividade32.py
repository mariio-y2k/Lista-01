saque = int(input("Digite o valor do saque (R$ 10 a R$ 600): "))

if saque < 10 or saque > 600:
    print("Valor inválido!")
else:
    notas100 = saque // 100
    resto = saque % 100

    notas50 = resto // 50
    resto = resto % 50

    notas10 = resto // 10
    resto = resto % 10

    notas5 = resto // 5
    resto = resto % 5

    notas1 = resto

    print("\nNotas fornecidas:")

    if notas100 > 0:
        print(f"Notas de R$ 100: {notas100}")

    if notas50 > 0:
        print(f"Notas de R$ 50: {notas50}")

    if notas10 > 0:
        print(f"Notas de R$ 10: {notas10}")

    if notas5 > 0:
        print(f"Notas de R$ 5: {notas5}")

    if notas1 > 0:
        print(f"Notas de R$ 1: {notas1}")
