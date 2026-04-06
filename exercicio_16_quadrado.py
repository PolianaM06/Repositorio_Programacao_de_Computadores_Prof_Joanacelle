# Leia um valor e: Mostre o tipo; 
#Se for numérico (após conversão) → mostre o quadrado.
n_str = input("Informe um valor:")
print (type(n_str))
n = float(n_str)
quad = n**2
print (quad)