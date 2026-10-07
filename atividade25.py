pequenas = int(input("Digite a quantidade de camisetas pequenas: "))
medias = int(input("Digite a quantidade de camisetas médias: "))
grandes = int(input("Digite a quantidade de camisetas grandes: "))

valor_pequenas = pequenas * 10
valor_medias = medias * 12
valor_grandes = grandes * 15

valor_total = valor_pequenas + valor_medias + valor_grandes

print(f"valor da compra: R$ {valor_total:.2f}")
