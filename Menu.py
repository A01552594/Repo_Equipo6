'''Se debera importar los archivos de los diferentes filtros con sus respectivos nombres.
    '''

import filtro1
import filtro2
import filtro3

def menu():
    nombre_imagen = input("Ingresa el nombre de la imagen a usar: ")
    print("\nFILTROS DISPONIBLES")
    print("1. Filtro 1")
    print("2. Filtro 2")
    print("3. Filtro 3")
    print("4. Salir")

def main():
    continua = True
    while continua:
        menu()
        opc_menu = int(input())
        if opc_menu == 1:
            filtro1(nombre_imagen)
        elif opc_menu == 2:
            filtro2(nombre_imagen)
        elif opc_menu == 3:
            filtro3(nombre_imagen)
        elif opc_menu == 4:
            break
main()