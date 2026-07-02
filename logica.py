from gestor_json import *
# 1) Traer datos desde JSON. Traer los datos del json y guardarlos en una colección

datos = cargar_datos()

def mostrar_datos(lista: list):
    for personaje in lista:
        for clave, valor in personaje.items():
            if clave == 'anio_nacimiento':
                print(f'Año de nacimiento: {valor} \n')
            elif type(valor) == list:
                print(f'Sus {clave} fueron: ')
                for logro in valor:
                    print(f'    ● {logro}')
                print('\n')
            else:
                print(f'{clave.capitalize()}: {valor} \n')

# 2) Listar los personajes de una época histórica en particular; 

#indices
    #0-nombre
    #1-epoca
    #2-pais
    #3-anio_nacimiento
    #4-profesion
    #5-logros[]
    #6-eventos[]


def listar_persojanes(coleccion: list) -> None:
    campo_a_filtrar = input(f'Campo a filtrar(nombre, epoca, pais, nacimiento, profesion, logros, eventos): ')
    dato_a_comparar = input(f'\nIngrese el dato que desea filtrar: ')

    for elemento in coleccion:
        if  elemento[campo_a_filtrar] == dato_a_comparar:
            mostrar_datos([elemento])


# 3) Modificar personaje de la lista (se le pedirá un nombre al usuario y si existe podrá modificarle algún dato que el usuario quiera) Ejemplo:
        # ● personaje a modificar: Julio César
        # ● característica a modificar: pais
        # ● nuevo valor: Italia

def modificar_dato(coleccion: list) -> None:
    nombre = input(f'Nombre del personaje a modificar: ')
    dato_a_modificar = input(f'\nIngrese el dato que desea modificar: ')

    for i in range(len(coleccion)):
        if coleccion[i]['nombre'] == nombre:
            nuevo_dato = input(f'\nIngrese el nuevo dato: ')
            coleccion[i][dato_a_modificar] = nuevo_dato

    modificar_datos(coleccion)

# 4) Eliminar personaje por nombre (el usuario ingresa un nombre y lo intenta eliminar de la colección)

def eliminar_personaje(coleccion: list) -> None:
    nombre = input(f'Nombre del personaje a eliminar: ')

    for i in range(len(coleccion)):
        if coleccion[i]['nombre'] == nombre:
            print(f'{nombre} fue eliminado!')
            coleccion.pop(i)
            break

    modificar_datos(coleccion)

# 5) Ordenar la lista de personajes por todos estos criterios:
            # ● anio_nacimiento
            # ● nombre
            # ● epoca
        # El usuario ingresará alguno de los 3, y por ese criterio se creará UNA COPIA DE LA COLECCIÓN ORIGINAL y se ordenará esa.

def ordenar_lista(coleccion: list) -> None:
    copia_ordenada = coleccion
    criterio = input('''
                     Ingrese porque criterio desea ordenar la lista:
                        ● anio_nacimiento
                        ● nombre
                        ● epoca
                     ''')
    

    for i in  range(len(copia_ordenada) - 1):
        for j in range(1, len(copia_ordenada)):
            if copia_ordenada[i][criterio] > copia_ordenada[j][criterio]:
                aux = copia_ordenada[i]
                copia_ordenada[i] = copia_ordenada[j]
                copia_ordenada[j] = aux
                
    mostrar_datos(copia_ordenada)

ordenar_lista(datos)