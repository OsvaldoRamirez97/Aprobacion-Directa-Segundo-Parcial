# Enunciado/s:
# La Organización Internacional de Estudios Históricos está desarrollando una aplicación para
# administrar información sobre las figuras más influyentes de la historia de la humanidad.

# Cada personaje histórico registrado posee información sobre su nombre, época histórica, país
# de origen, año de nacimiento, profesión principal y otros datos relevantes. Además, para cada
# personaje se registran sus principales logros y los eventos históricos más importantes en los que
# participó.

# Los investigadores necesitan una herramienta que les permita consultar, modificar y
# administrar esta información de forma eficiente.
# Se solicita desarrollar una aplicación utilizando los contenidos vistos durante la cursada.
# Nos pidieron hacer una aplicación con un menú que contenga las siguientes opciones:
    # Consignas
        # 1) Traer datos desde JSON. Traer los datos del json y guardarlos en una colección

        # 2) Listar los personajes de una época histórica en particular; 
        # El usuario ingresará una época y se mostrarán todos los personajes pertenecientes a dicha época de manera amigable para el usuario.

        # 3) Modificar personaje de la lista (se le pedirá un nombre al usuario y si existe podrá modificarle algún dato que el usuario quiera) Ejemplo:
        # ● personaje a modificar: Julio César
        # ● característica a modificar: pais
        # ● nuevo valor: Italia

        # 4) Eliminar personaje por nombre (el usuario ingresa un nombre y lo intenta eliminar de la colección)

        # 5) Ordenar la lista de personajes por todos estos criterios:
            # ● anio_nacimiento
            # ● nombre
            # ● epoca
        # El usuario ingresará alguno de los 3, y por ese criterio se creará UNA COPIA DE LA COLECCIÓN ORIGINAL y se ordenará esa.

        # 6) Listar los datos completos del personaje que posea la mayor cantidad de logros registrados.

        # 7) Listar los datos completos del personaje que haya participado en la menor cantidad de eventos históricos.

        # 8) Salir (cuando salga debe guardar en el archivo los cambios hechos durante el programa
        # (modificación o eliminación) para así mantener una persistencia de los cambios)

    # Objetivos de Aprobación Directa (Calificación de 6 a 10 puntos):
    # ● Integración de todos los temas vistos en clase hasta el momento del parcial, sin usar librerías
    # ni recursos externos
    # ● Que todas las opciones funcionen de manera correcta y el código este escrito siguiendo todas
    # las buenas prácticas de la programación
    # ● Poder defender con lenguaje fluido y técnico el entregable

from gestor_json import *

datos = cargar_datos()
