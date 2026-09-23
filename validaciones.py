def pedir_consumo():
    """Pide un consumo numerico y no negativo."""
    while True:
        try:
            consumo = float(input("Consumo en kWh: "))
            if consumo < 0:
                print("El consumo no puede ser negativo.")
            else:
                return consumo
        except ValueError:
            print("Ingrese un numero valido.")


def pedir_posicion(registros):
    """Pide una posicion que exista en el arreglo."""
    if len(registros) == 0:
        print("No hay registros guardados.")
        return None

    try:
        posicion = int(input("Ingrese la posicion del registro: "))
    except ValueError:
        print("La posicion debe ser un numero entero.")
        return None

    if posicion < 0 or posicion >= len(registros):
        print("La posicion no existe.")
        return None
    return posicion
