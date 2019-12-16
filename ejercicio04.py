#ejercicio mientras
# DECLARAR
cantidad=0
cantidad_invalida=(cantidad<5 or cantidad>19)
while(cantidad_invalida):
    cantidad=int(input("Ingresar cantidad:"))
    cantidad_invalida=(cantidad<5 or cantidad>19)
#fin_while
print("cantidad invalida:",cantidad)
