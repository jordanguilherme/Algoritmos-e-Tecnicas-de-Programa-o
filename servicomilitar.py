#Programa que verifica disponibilidade militar

print ("Serviço Militar")
print (" ")
nome = input("Informe seu nome: ")
print(f"Olá, {nome}")
idade = int(input("Por favor, informe sua idade: "))
genero = int(input("Informe o gerêro da pessoa: (1 - Masculino 2 - Feminino): "))
#validacao dos dados
if idade < 18:
    print(f"O usuário {nome} não pode alistar.")
elif idade >=18 and idade <=21 and genero == 1:
    print(f"O Usuário {nome} deve se alistar.")
else:
    print("Você deve uma multinha para o Lulinha")
