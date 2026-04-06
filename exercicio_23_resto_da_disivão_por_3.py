#Leia três números inteiros informados pelo usuário. 
#Exiba em ordem decrescente o resto da divisão por 3.
a = int(input("Informe o primeiro número inteiro:"))
b = int(input("Informe o segundo número inteiro:"))
c = int(input("Informe o terceiro número inteiro:"))
if ((a%3)<=(b%3)) and ((a%3)<=(c%3)):
    if ((b%3)<=(c%3)):
        print (c%3, b%3, a%3)
    else:
        print (b%3, c%3, a%3)
elif ((b%3)<=(c%3)):
    if ((a%3)<=(c%3)):
        print (c%3, a%3, b%3)
    else:
        print (a%3, c%3, b%3)
else:
    if ((a%3)<=(b%3)):
        print (b%3, a%3, c%3)
    else:
        print (a%3, b%3, c%3)