'''Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de su nombre y la cantidad de películas de la saga en la que participó, implementar las funciones necesarias para resolver las siguientes actividades:
a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posición uno la cima de la pila;
b. determinar los personajes que participaron en más de 5 películas de la saga, además indicar la cantidad de películas en la que aparece;
c. determinar en cuantas películas participo la Viuda Negra (Black Widow);
d. mostrar todos los personajes cuyos nombre empiezan con C, D y G.'''

from pila import Stack

def posicion_personajes(pila, nombre1, nombre2):
    posicion_rocket = None
    posicion_groot = None
    auxiliar = Stack()
    posicion = 1

    while pila.size() > 0:
        personaje = pila.pop()
        if personaje['nombre'] == nombre1:
            posicion_rocket = posicion
        if personaje['nombre'] == nombre2:
            posicion_groot = posicion
        auxiliar.push(personaje)
        posicion += 1

    while auxiliar.size() > 0:
        pila.push(auxiliar.pop())

    return posicion_rocket, posicion_groot

def personajes_mas_de_5_peliculas(pila):
    personajes = []
    auxiliar = Stack()

    while pila.size() > 0:
        personaje = pila.pop()
        if personaje['peliculas'] > 5:
            personajes.append((personaje['nombre'], personaje['peliculas']))
        auxiliar.push(personaje)

    while auxiliar.size() > 0:
        pila.push(auxiliar.pop())

    return personajes

def peliculas_viuda_negra(pila, nombre):
    cantidad_peliculas = 0
    auxiliar = Stack()

    while pila.size() > 0:
        personaje = pila.pop()
        if personaje['nombre'] == nombre:
            cantidad_peliculas = personaje['peliculas']
        auxiliar.push(personaje)

    while auxiliar.size() > 0:
        pila.push(auxiliar.pop())

    return cantidad_peliculas

def personajes_letra_cdg(pila):
    personajes = []
    auxiliar = Stack()
    letras = {'C', 'D', 'G'}

    while pila.size() > 0:
        personaje = pila.pop()
        if personaje['nombre'][0] in letras:
            personajes.append(personaje['nombre'])
        auxiliar.push(personaje)

    while auxiliar.size() > 0:
        pila.push(auxiliar.pop())

    return personajes

pila_mcu = Stack()
pila_mcu.push({'nombre': 'Iron Man', 'peliculas': 10})
pila_mcu.push({'nombre': 'Thor', 'peliculas': 8})
pila_mcu.push({'nombre': 'Rocket Raccoon', 'peliculas': 4})
pila_mcu.push({'nombre': 'Groot', 'peliculas': 4})
pila_mcu.push({'nombre': 'Black Widow', 'peliculas': 9})
pila_mcu.push({'nombre': 'Hulk', 'peliculas': 6})
pila_mcu.push({'nombre': 'Captain America', 'peliculas': 11})
pila_mcu.push({'nombre': 'Doctor Strange', 'peliculas': 5})

pos_rocket, pos_groot = posicion_personajes(pila_mcu, 'Rocket Raccoon', 'Groot')
print(f'Rocket Raccoon está en la posición {pos_rocket}')
print(f'Groot está en la posición {pos_groot}')

personajes_5_peliculas = personajes_mas_de_5_peliculas(pila_mcu)
print('Personajes con más de 5 películas:', personajes_5_peliculas)

peliculas_bw = peliculas_viuda_negra(pila_mcu, 'Black Widow')
print(f'Viuda Negra participó en {peliculas_bw} películas')

personajes_cdg = personajes_letra_cdg(pila_mcu)
print('Personajes cuyos nombres empiezan con C, D y G:', personajes_cdg)