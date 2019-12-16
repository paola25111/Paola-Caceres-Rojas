#ejercicio interaccion
import os
fecha_de_nacimiento=os.sys.argv[2]
for letra in fecha_de_nacimiento:
    print(letra)
    print("#fecha de nacimiento#")
fecha_de_nacimiento="&#$="
for letra in fecha_de_nacimiento:
    if(letra=="&"):
        print("quince")
        print("#############")
    if(letra=="#"):
        print("de diciembre")
        print("###############")
    if (letra=="$"):
        print("del 2016")
    #fin if
#fin for
print("#########################")
