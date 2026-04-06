#Leia um número e:
#Se for positivo, mostre a raiz aproximada (use **0.5);
#Caso contrário, informe “Número inválido”
n = float(input("Digite um número:"))
if (n>0):
    raiz = (n**0.5)
    print ("A raiz aproximada do número é:", raiz)
else:
    print ("Número inválido.")