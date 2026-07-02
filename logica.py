from gestor_json import *
from validaciones import *
# 1) Traer datos desde JSON. Traer los datos del json y guardarlos en una colección

datos = cargar_datos()

def mostrar_datos(lista: list) -> None:
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

def listar_elementos(lista: list, categoria: str) -> list:
    lista_filtrada = []

    for elemento in lista:
        if elemento[categoria] not in lista_filtrada:
            lista_filtrada.append(elemento[categoria])

    return lista_filtrada

def listar_personajes(coleccion: list) -> None:

    lista_epocas = listar_elementos(coleccion, "epoca")

    epoca = validar_dato("época")

    while not validar_epoca(lista_epocas, epoca):
        print("Época inválida.")
        epoca = validar_dato("época")

    for personaje in coleccion:
        if personaje["epoca"].lower() == epoca.lower():
            mostrar_datos([personaje])


# 3) Modificar personaje de la lista (se le pedirá un nombre al usuario y si existe podrá modificarle algún dato que el usuario quiera) Ejemplo:
        # ● personaje a modificar: Julio César
        # ● característica a modificar: pais
        # ● nuevo valor: Italia

def modificar_dato(coleccion: list) -> None:

    nombre = validar_dato('nombre del personaje que desea modificar')

    while not validar_nombre(coleccion, nombre):
        print('El nombre ingresado no existe!')
        nombre = validar_dato('nombre del personaje que desea modificar')

    campo = ingresar_dato()

    while not validar_campo_modificable(campo):
        print("Campo inválido.")
        campo = ingresar_dato()

    nuevo_valor = validar_dato("nuevo valor")

    if campo == "anio_nacimiento":
        nuevo_valor = int(nuevo_valor)

    for personaje in coleccion:

        if personaje["nombre"].lower() == nombre.lower():
            personaje[campo] = nuevo_valor
            break
    modificar_datos(coleccion)


# 4) Eliminar personaje por nombre (el usuario ingresa un nombre y lo intenta eliminar de la colección)

def eliminar_personaje(coleccion: list) -> None:
    nombre = validar_dato('nombre del personaje a eliminar')

    while not validar_nombre(coleccion, nombre):
        print("Ese personaje no existe.")
        nombre = validar_dato("nombre del personaje")

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
    copia_ordenada = coleccion.copy()
    orden_epocas = {
    "Antiguedad": 1,
    "Renacimiento": 2,
    "Edad Moderna": 3,
    "Edad Contemporanea": 4
    }
    criterio = validar_dato("criterio")

    while not validar_criterio(criterio):
        print("Criterio inválido.")
        criterio = validar_dato("criterio")

    for i in range(len(copia_ordenada) - 1):

        for j in range(i + 1, len(copia_ordenada)):

            if criterio == "epoca":

                if orden_epocas[copia_ordenada[i]["epoca"]] > orden_epocas[copia_ordenada[j]["epoca"]]:
                    copia_ordenada[i], copia_ordenada[j] = copia_ordenada[j], copia_ordenada[i]

            else:

                if copia_ordenada[i][criterio] > copia_ordenada[j][criterio]:
                    copia_ordenada[i], copia_ordenada[j] = copia_ordenada[j], copia_ordenada[i]

    for personaje in copia_ordenada:
        print(personaje[criterio])