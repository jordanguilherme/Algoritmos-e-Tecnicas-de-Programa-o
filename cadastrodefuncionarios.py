#Uma empresa precisa cadastrar os salários de seus funcionários, ao final do cadastro, devem ser apresentados as seguintes informações:
# Somatório total dos salários
# Média salarial
# O maior salário cadastrado e o menor salário cadastrado.
# Escreva um programa em python que atenda a esses requisitos.


#Variavéis para armazenar as informações

total_salarios = 0
maior_salario = 0
menor_salario = float('inf')

numero_funcionarios = 0

while True:
    salario = float(input("Informe o salário do funcionário: "))

    total_salarios += salario
    numero_funcionarios += 1

    if salario > maior_salario:
        maior_salario = salario

    if salario < menor_salario:
        menor_salario = salario

    pergunta = input("Deseja cadastrar outro salário? (s/n): ").lower()
    if pergunta != "s":
        break

# Cálculo da média salarial
if numero_funcionarios > 0:
    media_salarial = total_salarios / numero_funcionarios
else:
    media_salarial = 0

# Apresentação dos resultados
print("\nResultados do Cadastro de Salários")
print(f"Somatório total dos salários: R$ {total_salarios:.2f}")
print(f"Média salarial: R$ {media_salarial:.2f}")
print(f"Maior salário cadastrado: R$ {maior_salario:.2f}")
print(f"Menor salário cadastrado: R$ {menor_salario:.2f}")