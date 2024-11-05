from heap import HeapMax, HeapMin

#personajes de MCU: nombre, superhéroe, género
personajes_ucm = [
    {"nombre": "Tony Stark", "heroe": "Iron Man", "genero": "M"},
    {"nombre": "Steve Rogers", "heroe": "Capitán América", "genero": "M"},
    {"nombre": "Natasha Romanoff", "heroe": "Black Widow", "genero": "F"},
    {"nombre": "Carol Danvers", "heroe": "Capitana Marvel", "genero": "F"},
    {"nombre": "Scott Lang", "heroe": "Ant-Man", "genero": "M"},
    {"nombre": "Thor Odinson", "heroe": "Thor", "genero": "M"}
]

# Crear el heap min para mantener los personajes organizados por nombre
heap_min = HeapMin()

# Insertar los personajes en el heap con prioridad según el nombre del personaje (alfabéticamente)
for personaje in personajes_ucm:
    heap_min.arribo(personaje, ord(personaje["nombre"][0]))


#A. Determinar el nombre del personaje de la superhéroe Capitana Marvel
print("A.")
print("Personaje de Capitana Marvel:", heap_min.encontrar_personaje_por_heroe(heap_min, "Capitana Marvel"))

#B. Mostrar los nombres de los superhéroes femeninos
print("\nB.")
print("Superhéroes femeninos:")
heap_min.mostrar_superheroes_femeninos(heap_min)

#C. Mostrar los nombres de los personajes masculinos
print("\nC.")
print("Personajes masculinos:")
heap_min.mostrar_personajes_masculinos(heap_min)

#D. Determinar el nombre del superhéroe del personaje Scott Lang
print("\nD.")
print("Superhéroe de Scott Lang:", heap_min.encontrar_heroe_por_personaje(heap_min, "Scott Lang"))

# E. Mostrar todos los datos de los superhéroes o personajes cuyos nombres comienzan con 'S'
print("\nE.")
print("Personajes y superhéroes que comienzan con 'S':")
heap_min.mostrar_personajes_por_inicial(heap_min, 'S')

# F. Determinar si Carol Danvers está en el heap e indicar su superhéroe
print("\nF:")
print("Superhéroe de Carol Danvers:", heap_min.encontrar_carol_danvers(heap_min))