import json

def cargar_datos () -> json:
    with open('historia.json', 'r') as archivo: 
        data = json.load(archivo)
    return data

def modificar_datos(datos:list) -> json:
    with open('historia.json', 'w') as archivo:
        json.dump(datos, archivo, indent=4)