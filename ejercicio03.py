#ejercicio mientras
# DECLARAR
precio=0
precio_invalido=(precio<5 or precio>55)
while(precio_invalido):
    precio=int(input("Ingresar precio:"))
    precio_invalido=(precio<5 or precio>55)
#fin_while
print("precio invalido:",precio)
