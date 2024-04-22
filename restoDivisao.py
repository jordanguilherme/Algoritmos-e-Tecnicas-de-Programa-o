x = 0
quantidade = 0 #variavel contadora
somatorio = 0 #variavel acumuladora
while x <= 2250:
    if x%2 == 0 :
        quantidade += 1
        somatorio += x
        print (x)
    x += 1
print(f"Foram encontrados {quantidade} números pares.")
print(f"A soma total dos números pares é {somatorio}.")