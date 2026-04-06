#Leia um número e: Se for maior que 100 → mostre metade;
#Senão → mostre o dobro.
n = float(input("Informe um número:"))
if (n>100):
    metade = (n/2)
    print ("A metade do número é:", metade)
else:
    dobro = (n*2)
    print ("O dobro do número é:", dobro)