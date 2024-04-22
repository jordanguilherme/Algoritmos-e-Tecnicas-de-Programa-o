#entrada de dados para os valores
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
#entradas condicionais
#caso 1 - mostrar o quadrado da soma
if num1 > num2:
    soma = num1 + num2 
    print(f"O quadrado da soma dos números é {soma**2}")
#caso 2 - mostrar a soma dos quadrados
elif num2 > num1:
    resultado = num1**2 + num2 **2
    print(f"A Soma dos quadrados é {resultado}")
else:
    print("Os números são iguais!")

    
    