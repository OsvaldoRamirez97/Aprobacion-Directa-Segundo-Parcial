from gestor_json import *
from logica import *

def mostrar_menu() -> None:
    print("""
==================== PERSONAJES HISTÓRICOS ====================

1 - Mostrar todos los personajes
2 - Listar personajes por época
3 - Modificar personaje
4 - Eliminar personaje
5 - Ordenar personajes
6 - Salir

===============================================================
""")


def main():

    datos = cargar_datos()

    opcion = 0

    while opcion != 6:

        mostrar_menu()

        try:
            opcion = int(input("Ingrese una opción: "))
        except ValueError:
            print("Debe ingresar un número.\n")
            continue

        match opcion:

            case 1:
                mostrar_datos(datos)

            case 2:
                listar_personajes(datos)

            case 3:
                modificar_dato(datos)
                datos = cargar_datos()

            case 4:
                eliminar_personaje(datos)
                datos = cargar_datos()

            case 5:
                ordenar_lista(datos)

            case 6:
                print("Programa finalizado.")

            case _:
                print("Opción inválida.")

main()