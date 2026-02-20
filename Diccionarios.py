#Nuevo diccionario

DB = {
    "pepe" : {"name" : "Pepe", "age" : 10},
    "paco" : {"name" : "Paco", "age" : 12},
    "luis" : {"name" : "Luis", "age" : 11},
    "renata" : {"name" : "Renata", "age" : 10}
}

#print(DB["renata"])

inventario = {
    "rojas" : {"Manzanas rojas" : 23},
    "amarillas" : {"Manzanas amarillas" : 25},
    "verdes" : {"Manzanas verdes" : 10},
    "peras" : {"Peras" : 14},
    "guayabas" : {"Guayabas" : 16},
    "melon" : {"Melon" : 3},
    "papaya" : {"Papaya" : 4},
    "platano" : {"Platano" : 6}
}

def busqueda_dic(inventario, indice):
    if nombre in inventario:
        return inventario.get(indice)
    else:
        return "No se encuentra registrado"


nombre = input(f"Ingrese el nombre de la fruta: ").lower()

print(busqueda_dic(inventario, nombre))