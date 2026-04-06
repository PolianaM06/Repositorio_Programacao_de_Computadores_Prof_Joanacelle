#Leia dois números informados pelo usuário.
#Se ambos forem positivos, calcule e exiba a soma entre eles.
#Caso contrário, calcule e exiba o produto entre eles.
a = float(input("Informe o primeiro número:"))
b = float(input("Informe o segundo número:"))
if (a>0) and (b>0):
    soma = (a+b)
    print ("A soma entre eles é:", soma)
else:
    produto = (a*b)
    print ("O produto entre eles é:", produto)