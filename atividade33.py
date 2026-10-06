numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

print("Escolha uma operação:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

operacao = int(input("Digite a operação: "))

if operacao == 1:
    resultado = numero1 + numero2
elif operacao == 2:
    resultado = numero1 - numero2
elif operacao == 3:
    resultado = numero1 * numero2
elif operacao == 4:
    if numero2 != 0:
        resultado = numero1 / numero2
    else:
        print("Não é possível dividir por zero.")
        resultado = None
else:
    print("Operação inválida.")
    resultado = None

if resultado is not None:
    print(f"\nResultado: {resultado}")

    if resultado % 2 == 0:
        print("O resultado é par.")
    else:
        print("O resultado é ímpar.")

    if resultado >= 0:
        print("O resultado é positivo.")
    else:
        print("O resultado é negativo.")

    if resultado.is_integer():
        print("O resultado é inteiro.")
    else:
        print("O resultado é decimal.")
