altura = float(input("Digite sua altura em metros: "))
sexo = input("Digite seu sexo (M/F): ").upper()

if sexo == "M":
    peso_ideal = (72.7 * altura) - 58
else:
    peso_ideal = (62.1 * altura) - 44.7

print(f"Seu peso ideal é: {peso_ideal:.2f} kg")
