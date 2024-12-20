from arbol_avl import ArbolBinario

# Creación de los árboles AVL específicos para cada índice
arbol_nombre = ArbolBinario()
arbol_numero = ArbolBinario()
arbol_tipo = ArbolBinario()

pokemons = [
    {"nombre": "Bulbasaur", "numero": 1, "tipo": ["planta", "veneno"]},
    {"nombre": "Charmander", "numero": 4, "tipo": ["fuego"]},
    {"nombre": "Squirtle", "numero": 7, "tipo": ["agua"]},
    {"nombre": "Jolteon", "numero": 135, "tipo": ["eléctrico"]},
    {"nombre": "Lycanroc", "numero": 745, "tipo": ["roca"]},
    {"nombre": "Tyrantrum", "numero": 697, "tipo": ["roca", "dragón"]}
]

# Inserción de los datos en los tres árboles
for pokemon in pokemons:
    arbol_nombre.insertar_por_nombre(pokemon["nombre"], pokemon)
    arbol_numero.insertar_por_numero(pokemon["numero"], pokemon)
    for tipo in pokemon["tipo"]:
        arbol_tipo.insertar_por_tipo(tipo, pokemon)

# A. Los índices de cada uno de los árboles deben ser nombre, número y tipo.

# B. Mostrar todos los datos de un Pokémon a partir de su número y nombre -para este último, la búsqueda debe ser por proximidad, es decir si busco “bul” se deben mostrar todos los Pokémons cuyos nombres comiencen o contengan dichos caracteres–.
numero_buscado = 4  # Ejemplo: número del Pokémon Charmander
print("A:\nBúsqueda por número:")
datos_pokemon_numero = arbol_numero.buscar_por_numero(numero_buscado)
print(f"Nombre: {datos_pokemon_numero["nombre"]}\nNúmero: {datos_pokemon_numero["numero"]}\nTipo/Tipos:")
for tipo in datos_pokemon_numero["tipo"]:
    print(" ", tipo)

nombre_aproximado = "bul"
print("\nB:\nBúsqueda por nombre aproximado:")
pokemons_aproximados = arbol_nombre.buscar_por_nombre_aproximado(nombre_aproximado)
for pokemon in pokemons_aproximados:
    print(f"Nombre: {pokemon["nombre"]}\nNúmero: {pokemon["numero"]}\nTipo/Tipos:")
    for tipo in pokemon["tipo"]:
        print(" ", tipo)

# C. Mostrar todos los nombres de todos los Pokémons de un determinado tipo agua, fuego, planta y eléctrico.
tipos_deseados = ["agua", "fuego", "planta", "eléctrico"]
print("\nC:\nPokémon de tipos específicos:")
for tipo in tipos_deseados:
    print(f"Tipo {tipo}:")
    pokemons_tipo = arbol_tipo.listar_por_tipo(tipo)
    for pokemon in pokemons_tipo:
        print(" ", pokemon["nombre"])

# D. Realizar un listado en orden ascendente por número y nombre de Pokémon, y además un listado por nivel por nombre.
print("\nD.I. Listado en orden ascendente por número:")
pokemons_ascendente_numero = arbol_numero.listar_ascendente()
print("--------------------")
for indice, pokemon in enumerate(pokemons_ascendente_numero):
    print(f"Nombre: {pokemon["nombre"]}\nNúmero: {pokemon["numero"]}\nTipo/Tipos:")
    for tipo in pokemon["tipo"]:
        print(" ", tipo)
    print("--------------------")

print("\nD.II. Listado en orden ascendente por nombre:")
pokemons_ascendente_nombre = arbol_nombre.listar_ascendente()
print("--------------------")
for pokemon in pokemons_ascendente_nombre:
    print(f"Nombre: {pokemon["nombre"]}\nNúmero: {pokemon["numero"]}\nTipo/Tipos:")
    for tipo in pokemon["tipo"]:
        print(" ", tipo)
    print("--------------------")

print("\nD.III. Listado por nivel:")
pokemons_por_nivel = arbol_nombre.listar_por_nivel()
print("--------------------")
for pokemon in pokemons_por_nivel:
    print(f"Nombre: {pokemon["nombre"]}\nNúmero: {pokemon["numero"]}\nTipo/Tipos:")
    for tipo in pokemon["tipo"]:
        print(" ", tipo)
    print("--------------------")

# E. Mostrar todos los datos de los Pokémons: Jolteon, Lycanroc y Tyrantrum.
pokemons_especificos = ["Jolteon", "Lycanroc", "Tyrantrum"]
print("\nE:\nDatos de Pokémon específicos:")
for nombre in pokemons_especificos:
    datos_pokemon = arbol_nombre.buscar_por_nombre_aproximado(nombre)
    for pokemon in datos_pokemon:
        print(f"Nombre: {pokemon["nombre"]}\nNúmero: {pokemon["numero"]}\nTipo/Tipos:")
        for tipo in pokemon["tipo"]:
            print(" ", tipo)

# F. Determina cuantos Pokémons hay de tipo eléctrico y acero.
tipos_contar = ["eléctrico", "acero"]
print("\nF:\nCantidad de Pokémon por tipo:")
for tipo in tipos_contar:
    cantidad = arbol_tipo.contar_pokemons_por_tipo(tipo)
    print(f"Tipo {tipo}: {cantidad}")