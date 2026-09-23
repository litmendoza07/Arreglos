from calculos import calcular_promedio, calcular_total
from validaciones import pedir_consumo, pedir_posicion


def mostrar_registros(registros):
    if len(registros) == 0:
        print("No hay registros guardados.")
        return

    print("\n--- Registros de consumo ---")
    for posicion, registro in enumerate(registros):
        print(
            f"{posicion}. Aparato: {registro['aparato']} | "
            f"Consumo: {registro['consumo']:.2f} kWh"
        )


def crear(registros):
    print("\n--- Crear registro ---")
    aparato = input("Nombre del aparato: ").strip()
    if aparato == "":
        print("El nombre no puede estar vacio.")
        return

    registro = {"aparato": aparato, "consumo": pedir_consumo()}
    registros.append(registro)
    print("Registro creado correctamente.")


def consultar(registros):
    print("\n--- Consultar registros ---")
    mostrar_registros(registros)


def actualizar(registros):
    print("\n--- Actualizar registro ---")
    mostrar_registros(registros)
    posicion = pedir_posicion(registros)
    if posicion is None:
        return

    aparato = input("Nuevo nombre del aparato: ").strip()
    if aparato == "":
        print("El nombre no puede estar vacio.")
        return

    registros[posicion] = {
        "aparato": aparato,
        "consumo": pedir_consumo()
    }
    print("Registro actualizado correctamente.")


def eliminar(registros):
    print("\n--- Eliminar registro ---")
    mostrar_registros(registros)
    posicion = pedir_posicion(registros)
    if posicion is None:
        return

    registros.pop(posicion)
    print("Registro eliminado correctamente.")


def mostrar_resumen(registros):
    print("\n--- Resumen de consumo ---")
    if len(registros) == 0:
        print("No hay registros guardados.")
        return

    print(f"Consumo total: {calcular_total(registros):.2f} kWh")
    print(f"Consumo promedio: {calcular_promedio(registros):.2f} kWh")


def mostrar_menu():
    print("\n=== CONSUMO ELECTRICO ===")
    print("1. Crear registro")
    print("2. Consultar registros")
    print("3. Actualizar registro")
    print("4. Eliminar registro")
    print("5. Ver resumen")
    print("6. Salir")


def ejecutar_programa():
    registros = []

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            crear(registros)
        elif opcion == "2":
            consultar(registros)
        elif opcion == "3":
            actualizar(registros)
        elif opcion == "4":
            eliminar(registros)
        elif opcion == "5":
            mostrar_resumen(registros)
        elif opcion == "6":
            print("Programa finalizado.")
            break
        else:
            print("Opcion no valida.")
