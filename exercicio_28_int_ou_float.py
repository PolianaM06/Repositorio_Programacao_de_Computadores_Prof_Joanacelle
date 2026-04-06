#Leia um valor informado pelo usuário. Verifique o tipo da variável; 
#Caso seja possível interpretá-lo como um valor numérico: 
#Se for um número inteiro, exiba o dobro;
#Caso seja um número real, exiba a metade;
#Caso não seja possível interpretar como número, exiba: “Tipo inválido”.
n_str = input("Informe um valor:")
try:
    n_int = int(n_str)
    print(n_int*2)
except ValueError:
    try:
        n_float = float(n_str)
        print(n_float/2)
    except ValueError:
        print("Tipo inválido.")