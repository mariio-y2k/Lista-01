salario = 1200.00
conta1 = 200.00
conta2 = 120.00

multa1 = conta1 * 2 / 100
multa2 = conta2 * 2 / 100

valor_conta1 = conta1 + multa1
valor_conta2 = conta2 + multa2

total_contas = valor_conta1 + valor_conta2
restante = salario - total_contas

print(f"Valor da conta 1 com multa: R$ {valor_conta1:.2f}")
print(f"Valor da conta 2 com multa: R$ {valor_conta2:.2f}")
print(f"Total pago nas contas: R$ {total_contas:.2f}")
print(f"Valor restante do salário: R$ {restante:.2f}")
