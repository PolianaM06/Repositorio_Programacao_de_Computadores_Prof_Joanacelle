#Leia dois números e exiba qual é o maior.
a = float(input("Digite o primeiro número:"))
b = float(input("Digite o segundo número:"))
if(a>b):
    print("O maior número é:", a)
elif(a==b):
    print("São iguais.")
else:
    print("O maior número é:", b)