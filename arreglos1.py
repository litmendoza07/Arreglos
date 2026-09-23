vector = []
vector.append(2)
vector.append(5)
vector.append(6)
print(len(vector))
#Tamaño
print("Tamaño", len(vector))

#Mostrar el doble de cada elemento 
print("""Doble de cada elemento, Esto es el resultado""")
for i in range(len(vector)):
    if i != len(vector) - 1:
        print(vector[i] * 2, end=", ")
    else:
        print(f"{vector[i] * 2}")

#Añadir en la posición 1 
vector.insert(1, "Jose")
print(vector)

#Añadir en la posición 0
vector.insert(0, "Mi esposa")
print(vector)

#Añadir en la posición 0 nuevamente
vector.insert(0, "Jesucristo")
print(vector)

#Modificar la segunda posición
vector[1] = "Santa Maria"
print(vector)

print("Eliminar el elemento")
vector.remove("Jose")
print(vector)

print("Eliminar por posicion")
del vector[2]
print(vector)

print("Eliminar el último elemento")
vector.pop()
print(vector)


