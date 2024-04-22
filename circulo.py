#importa o modulo pi da biblioteca math
from math import pi

raio = float(input("Informe o raio do círculo: "))
#validando o raio do circulo
if raio > 0:
    area = pi * (raio**2)
    #imprime o resultado da area
    print(f"A área do círculo é: {area:.2f}")
    
else: 
    print ("A medida do raio deve ser maior que zero. ")
