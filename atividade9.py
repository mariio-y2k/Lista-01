nome = input("digite seu nome: ")
disciplina = input("digite a disciplina: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3)/3

print(f"Sua média final é de: {media:.2f}")

if media >=6:
    print ("Aprovado!!!")
else:
    print ("Reprovado!!!")