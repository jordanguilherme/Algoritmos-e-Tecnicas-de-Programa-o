while True:
    #recebe notas dos alunos.
    nota1 = float(input("Digite o valor da nota 1: "))
    nota2 = float(input("Digite o valor da nota 2: "))
    nota3 = float(input("Digite o valor da nota 3: "))
    nota4 = float(input("Digite o valor da nota 4: "))
    #calculo do somatorio das notas
    soma = nota1 + nota2 + nota3 + nota4
    #calculo da média de notas
    media = soma/4
    #validação da aprovação de notas
    if media >= 6:
        print (f"O Aluno está aprovado com média {media:.1f}") #
    else:
        print (f"O Aluno está reprovado com média {media:.1f}") #o comando :.1f serve para exibir o numero de casas decimais desejadas (1f é 1 casa decimal, 2f são duas casas cimais...)
    opcao = input("Deseja cadastrar mais um aluno? (s/n)")
    if opcao.upper() !="s": #upper (maiusculo) ou lower (minusculo)
        break