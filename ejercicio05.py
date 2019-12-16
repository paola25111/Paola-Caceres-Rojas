#ejercicio mientras
# DECLARAR
numero=0
numero_invalido=(numero<50 or numero>100)
while(numero_invalido):
    numero=int(input("Ingresar numero:"))
    numero_invalido=(numero<50 or numero>100)
#fin_while
print("numero invalido:",numero)
