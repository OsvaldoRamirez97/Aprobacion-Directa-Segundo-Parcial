campos = {
    "nombre": "nombre",
    "epoca": "epoca",
    "pais": "pais",
    "nacimiento": "anio_nacimiento",
    "anio_nacimiento": "anio_nacimiento",
    "profesion": "profesion",
    "logros": "logros",
    "eventos": "eventos"
}


def validar_dato(texto: str = "dato") -> str:
    dato = input(f"Ingrese {texto}: ").strip()

    while dato == "":
        dato = input(f"{texto.capitalize()} no puede estar vacío: ").strip()

    return dato


def ingresar_dato() -> str:
    campo = validar_dato("campo").lower()

    while campo not in campos:
        print("Campo inválido.")
        campo = validar_dato("campo").lower()

    return campos[campo]


def validar_categoria(categoria: str) -> bool:
    return categoria in campos


def validar_epoca(lista_epocas: list, epoca: str) -> bool:
    for elemento in lista_epocas:
        if elemento.lower() == epoca.lower():
            return True

    return False


def validar_nombre(coleccion: list, nombre: str) -> bool:
    for personaje in coleccion:
        if personaje["nombre"].lower() == nombre.lower():
            return True

    return False


def validar_criterio(criterio: str) -> bool:
    return criterio in (
        "nombre",
        "epoca",
        "anio_nacimiento"
    )


def validar_campo_modificable(campo: str) -> bool:
    return campo in (
        "nombre",
        "epoca",
        "pais",
        "anio_nacimiento",
        "profesion",
        "logros",
        "eventos"
    )