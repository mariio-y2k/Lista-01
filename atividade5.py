nome = input("Digite seu nome: ")
disciplina = input ("Digite sua disciplina: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3)/3

print(f"Seu nome: {nome}\nDisciplina: {disciplina}\nSua nota é: {media:.2f}")