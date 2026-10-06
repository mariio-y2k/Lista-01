paes = int(input("Digite a quantidade de pães vendidos: "))
broas = int(input("Digite a quantidade de broas vendidas: "))

valor_paes = paes * 1.00
valor_broas = broas * 3.50

total_arrecadado = valor_paes + valor_broas
poupanca = total_arrecadado * 10 / 100

print(f"Total arrecadado: R$ {total_arrecadado:.2f}")
print(f"Valor para guardar na poupança: R$ {poupanca:.2f}")
