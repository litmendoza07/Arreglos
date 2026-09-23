def calcular_total(registros):
    """Calcula el consumo total del arreglo."""
    total = 0
    for registro in registros:
        total += registro["consumo"]
    return total


def calcular_promedio(registros):
    """Calcula el promedio del consumo."""
    if len(registros) == 0:
        return 0
    return calcular_total(registros) / len(registros)
