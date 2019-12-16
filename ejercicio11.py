#ejercicio interaccion
import os
msg=os.sys.argv[1]
for letra in msg:
    print(letra)
msg="#$I."
for letra in msg:
    if(letra=="#"):
        print("llamame")
        print("#############")
    if(letra=="$"):
        print("naceito dinero")
        print("###############")
    if (letra=="I"):
        print("Urgente")
    #fin if
#fin for
print("#########################")
