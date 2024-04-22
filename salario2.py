#programa de cadastro de salarios
quantFuncionarios = 0 #total de funcionarios
totalSalarios = 0 #somatorio os salarios

opcao = "s"
while True: 
    if opcao == "s":
        salario = float(input ("Informe o salário do funcionário: "))
        totalSalarios += salario
        quantFuncionarios += 1
        opcao = input("Deseja cadastrar mais um funcionário?(s/n): ")
    else:
        break
    
print (f"A Soma total dos salários é: R$ {totalSalarios:.2f}")
print (f"A empresa pagou para {quantFuncionarios}  funcionários.")

    