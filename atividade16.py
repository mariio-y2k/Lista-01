numero_1 = float(input("Digite o primeiro numero: "))
numero_2 = float(input("Digite o segundo numero: "))
numero_3 = float(input("Digite o terceiro numero: "))

if numero_1 >= numero_2 and numero_1 >= numero_3:
    maior = numero_1
elif numero_2 >= numero_3 and numero_2 >= numero_1:
    maior = numero_2
else: 
    maior = numero_3

if numero_1 <= numero_2 and numero_1 <= numero_3:
    menor = numero_1
elif numero_2 <= numero_3 and numero_2 <= numero_1:
    menor = numero_2
else: 
    menor = numero_3

print(f"Maior: {maior}")
print(f"Menor: {menor}")