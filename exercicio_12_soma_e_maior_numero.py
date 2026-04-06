#Leia dois números e: Mostre a soma; 
#Mostre qual é maior ou se são iguais.
a = float(input("Informe o primeiro número:"))
b = float(input("Informe o segundo número:"))
soma = a+b
if (a>b):
    print("A soma é:", soma ,"E o maior número é:", a)
elif (a<b):
     print("A soma é:", soma ,"E o maior número é:", b)
else:
      print("A soma é:", soma ,"E os números são iguais.")