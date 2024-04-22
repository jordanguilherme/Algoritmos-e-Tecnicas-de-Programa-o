idade = int(input("Digite sua idade: "))
if idade < 16:
    print("Você não pode votar!")
elif idade <18 or idade >=70:
    print("Seu voto é opcional!")
else:
    print("Seu voto é obrigatório")



