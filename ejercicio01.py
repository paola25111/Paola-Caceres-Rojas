#ejercicio mientras
# DECLARAR
edad=0
edad_invalida=(edad<18 or edad>100)
while(edad_invalida):
    edad=int(input("Ingresar edad:"))
    edad_invalida=(edad<18 or edad>100)
#fin_while
print("edad invalida:",edad)
