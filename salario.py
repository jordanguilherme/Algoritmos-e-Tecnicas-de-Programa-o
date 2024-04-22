#programa de cadastro de salarios
quantFuncionarios = 0 #total de funcionarios
totalSalarios = 0 #somatorio os salarios

quantidade = int(input("Quantos funcionários deseja cadastrar? "))
cont = 0 #conta os funcionarios ate a quantidade desejada

while cont < quantidade: 
    salario = float(input ("Informe o salário do funcionário: "))
    totalSalarios += salario
    cont += 1
print (f"A Soma total dos salários é: R$ {totalSalarios:.2f}")

    