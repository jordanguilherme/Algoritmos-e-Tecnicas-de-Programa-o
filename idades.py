"""SOMA DAS IDADES
MEDIA DAS IDADES
MENOR IDADE CADASTRADA
MAIOR IDADE CADASTRADA"""
cont = 0 #VARIAVEL CONTADORA
soma = 0 #VARIAVEL ACUMULADORA - ARMAZENA O TOTAL DAS IDADES
menor_idade = 1000 
maior_idade = 0
while cont < 5:
    idade = int(input("Digite a idade desejada: "))
    soma += idade #soma = soma + idade (soma recebe ela própria + idade)
    #encontrando a menor idade cadastrada
    if idade < menor_idade:
        menor_idade = idade
    cont += 1 #cont = cont + 1 (cont recebe cont + 1)
    if idade > maior_idade:
        maior_idade = idade
    
print(f"O somatório total das idades é {soma}")
media = soma/cont
print(f"A média das idades cadastradas é {media}")
print(f"A menor idade cadastrada é {menor_idade}")
print(f"A Maior idade cadastrada é {maior_idade}")
