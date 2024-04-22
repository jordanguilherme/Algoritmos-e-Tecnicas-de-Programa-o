print("Escola Pingo de Gente\n Sistema de Notas")
aluno = input("Informe do nome do aluno: ")
print(f"Informe as notas do aluno {aluno}")
nota1 = float(input("1ª nota: "))
nota2 = float(input("2ª nota: "))
nota3 = float(input("3ª nota: "))
media = (nota1+nota2+nota3)/3
print(f"A média final do aluno {aluno} é {media}")