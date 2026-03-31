#Dados três números inteiros, impria o menor dele.
a = int(input("Digite o primeiro número:"))
b = int(input("Digite o segundo número:"))
c = int(input("Digite o terceiro número:"))
if(a<=b) and (a<=c):
    print("O menor número é", a)
elif(b<=a) and (b<=c):
    print("O menor número é", b)
else:
    print("O menor número é", c)