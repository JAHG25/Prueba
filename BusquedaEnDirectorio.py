#Busqueda en directorio



def lineal(lista, item):
    count = 0
    posicion = 0
    while posicion < len(lista):
        if lista[posicion] != item:
            posicion += 1
            count += 1
        elif lista[posicion] == item:
            print(f"""Pasos para llegar al resultado(l): {count}""")
            return posicion
        else:
            return None