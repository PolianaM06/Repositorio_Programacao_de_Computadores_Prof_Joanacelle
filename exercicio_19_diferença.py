#Leia dois números e: 
#Verifique se são iguais ou diferentes.
#Sendo diferentes mostre a diferença entre eles.
a = float(input("Digite o primeiro número:"))
b = float(input("Digite o segundo número:"))
if (a!=b):
    sub = (a-b)
    print ("Os nùmeros são diferentes e a diferença é:", sub)
else:
    print ("Os números são iguais.")