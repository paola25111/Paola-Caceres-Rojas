#ejercicio mientras
# DECLARAR
peso=0
peso_invalido=(peso<30 or peso>70)
while(peso_invalido):
    peso=int(input("Ingresar peso:"))
    peso_invalido=(peso<30 or peso>70)
#fin_while
print("peso Invalido:",peso)
