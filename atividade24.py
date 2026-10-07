sanduiches = int(input("Digite a quantidade de sanduíches: "))

queijo = sanduiches * 2 * 50
presunto = sanduiches * 50
carne = sanduiches * 100

queijo = queijo / 1000
presunto = presunto / 1000
carne = carne / 1000

print(f"queijo necessário: {queijo:.2f} kg")
print(f"presunto necessário: {presunto:.2f} kg")
print(f"carne necessária: {carne:.2f} kg")
