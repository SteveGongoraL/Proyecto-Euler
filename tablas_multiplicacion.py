#ejercicio con tablas de multiplicación

def tabla_automatica():
    for i in range(1,11):
        print(f"Tabla del {i}")
        for x in range(1,11):
            print(f"{i} x {x} = {i*x}")
        print()
def tabla_manual():
    num_eleccion = int(input("Dime el numero del que deseas saber la tabla de multiplicación: "))
    print(f"Tabla del {num_eleccion}")
    for i in range(1,11):
        print(f"{num_eleccion} x {i} = {num_eleccion*i}")
    print()

while True:
    op=int(input("¿Que opcion deseas realizar?: \n1) Ver las tablas del 1 al 10. \n2) Ver la tabla que tu decidas. \n3) Salir. \n"))
    if op == 1:
        tabla_automatica()
    elif op == 2:
        tabla_manual()   
    elif op == 3:
        break
    else:
        print("Debes escoger una opción valida.\n")
