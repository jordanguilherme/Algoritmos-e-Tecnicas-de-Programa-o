secreto = 32
while True: # While significa enquanto e true significa verdadeiro, (enquanto for verdadeiro)
    numero = int(input("Adivinhe o número: "))
    if numero < secreto:
        print("O número secreto é maior! ")
    elif numero > secreto:
        print("O número secreto é menor! ")
    else:
        print("Parabéns, você acertou!")
    break
