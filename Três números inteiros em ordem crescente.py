#Dados três números inteiros, imprima os número em ordem crescente
a = int(input("Digite o primeiro número:"))
b = int(input("Digite o segundo número:"))
c = int(input("Digite o terceiro número:"))
if(a<=b) and (a<=c):
    if (b<=c):
        print(a, b, c)
    else:
        print(a, c, b)
elif(b<=c):
    if(a<=c):
        print(b, a, c)
    else: (b, c, a)
else:
    if(a<=b):
        print(c, a, b)
    else:
        print(c, b, a)