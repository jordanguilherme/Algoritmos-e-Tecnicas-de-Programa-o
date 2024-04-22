#Jogo de adivinhação em python
#entrada de números

x = 52
while True:
 num1 = int(input("Digite um número aleatório: "))
 if  num1 > x :
    print('O numéro secreto é menor')
 elif  num1 < x :
    print('o numéro secreto é maior')
 else:
    num1=x
    print('parabéns!!!! Você adivinhou o numéro secreto!')
    break
