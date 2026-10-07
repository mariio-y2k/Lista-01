peso = float(input("Digite o peso dos peixes em kg: "))

if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
else:
    excesso = 0
    multa = 0

print(f"Excesso de peso: {excesso:.2f} kg")
print(f"Valor da multa: R$ {multa:.2f}")

