#Leia um número e: 
#Mostre se ele é par positivo, par negativo, 
#impar positivo, impar negativo ou neutro.
n = float(input("Informe um número:"))
if (n>0):
    if (n%2 == 0):
        print("Par positivo.")
    else:
        print("Ímpar positivo.")
elif (n<0):
    if (n%2 == 0):
        print("Par negativo.")
    else:
        print("Ímpar negativo.")
else:
    print ("Neutro.")