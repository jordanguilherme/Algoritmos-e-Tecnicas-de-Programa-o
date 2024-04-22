while True:
    print("""
            Programa de cálculo de áreas
            Menu - Digite a opção desejada
            1. Quadrado
            2. Retângulo
            3. Triângulo
            4. Trapézio
            5. Pentágono
            6. Círculo
            0. Sair
          """)
    opcao = int(input("Qual área deseja calcular? "))
    if opcao == 1:
        lado = float(input("Digite o lado do quadrado: "))
        area = lado ** 2
        print("A área do quadrado é: ",area)
        break    
    elif opcao == 2:
        comprimento = float(input("Escreva o comprimento do retângulo:  "))
        largura = float(input("Escreva a largura do retângulo: "))
        area = comprimento * largura
        print("A área do retângulo é: ",area)
        break
    elif opcao == 3:
        base = float(input("Escreva o valor da base do triângulo: "))
        altura = float(input("Escreva o valor da altura do triângulo: "))
        area = base * altura / 2
        print("A área do triângulo é: ", area)
        break
    elif opcao == 4:
        comprimento_base_maior = float(input("Escreva o comprimento da base maior: "))
        comprimento_base_menor = float(input("Escreva o comprimento da base menor: "))
        altura_trapézio = float(input("Escreva a altura do trapézio: "))
        area = (comprimento_base_maior + comprimento_base_menor) * altura_trapézio / 2
        print("A base do trapézio é :", area)
        break
    elif opcao == 5:
        import math
        lado = float(input("Escreva o comprimento de um lado do pentagono: "))
        raio = lado / (2 * math.sin ( math.pi / 5))
        print("O Raio do pentagono é : ",raio)
        break
    elif opcao == 6:
        import math
        raio = float(input("Escreva o valor do raio do circulo: "))
        if raio > 0:       
            area = math.pi * (raio * raio)
            print(" A área do círculo é: ",area)
        else:
            print("O Raio deve ser maior que zero.")
    elif opcao == 0:
        break
    else:
        print("Opção Inválida")