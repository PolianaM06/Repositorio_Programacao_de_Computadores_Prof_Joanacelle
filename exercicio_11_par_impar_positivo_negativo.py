#Leia um número e:
#Se for par e positivo → “Par positivo”;
#Se for par e negativo → “Par negativo”;
#Caso contrário → “Ímpar”.
n = float(input("Informe um número:"))
if(n%2 == 0):
    if(n>0):
        print("Par positivo.")
    else:
        print("Par negativo.")
else:
    print ("Impar.")