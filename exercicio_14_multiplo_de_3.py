#Leia um valor e: Converta para inteiro;
# Se for múltiplo de 3 → “Múltiplo de 3”;
# Senão → “Não é múltiplo”.
n_str = input("Digite um valor:")
n = int(n_str)
if (n%3 == 0):
    print ("Múltiplo de 3.")
else:
    print ("Não é múltiplo.")