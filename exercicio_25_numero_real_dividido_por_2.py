#Leia um valor informado pelo usuário. Exiba o tipo da variável lida. 
#Verifique se é possível converter o valor para número real (float). 
#Se for possível, exiba o resultado da divisão desse número por 2. 
#Caso contrário, exiba: “Não numérico”.
try:
    n = float(input("Informe um valor:"))
    metade = n/2
    print ("O número dividido por 2 é:", metade)
except ValueError:
    print ("Não númerico.")