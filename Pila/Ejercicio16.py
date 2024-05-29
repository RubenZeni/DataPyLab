'''Se tienen dos pilas con personajes de Star Wars, en una los del episodio V de “The empire strikes back” y la otra los del episodio VII “The force awakens”. Desarrollar un algoritmo que permita obtener la intersección de ambas pilas, es decir los personajes que aparecen en ambos episodios.'''

from pila import Stack

def interseccion_pilas(pila1, pila2):
    auxiliar1 = Stack() # Para restaurar 
    auxiliar2 = Stack()
    auxiliar3 = Stack()  # Para restaurar pila2
    interseccion = Stack()
    elementos_interseccion = []

    # Mover elementos de pila1 a auxiliar1 (y restaurar pila1)
    while pila1.size() > 0:
        elemento = pila1.pop()
        auxiliar1.push(elemento)
    
    while auxiliar1.size() > 0:
        elemento = auxiliar1.pop()
        pila1.push(elemento)
        auxiliar2.push(elemento)

    # Verificar la intersección con pila2 y almacenar en intersección
    while pila2.size() > 0:
        elemento = pila2.pop()
        auxiliar3.push(elemento)  # Guardar elemento de pila2 para restaurar después
        
        esta_en_pila1 = False
        while auxiliar2.size() > 0:
            aux_elemento = auxiliar2.pop()
            auxiliar1.push(aux_elemento)
            if aux_elemento == elemento:
                esta_en_pila1 = True
        
        # Restaurar auxiliar2
        while auxiliar1.size() > 0:
            auxiliar2.push(auxiliar1.pop())
        
        if esta_en_pila1 and elemento not in elementos_interseccion:
            elementos_interseccion.append(elemento)
    
    # Restaurar pila2
    while auxiliar3.size() > 0:
        pila2.push(auxiliar3.pop())

    # Crear la pila de intersección
    for elemento in elementos_interseccion:
        interseccion.push(elemento)
    
    return interseccion

pila_episodio_v = Stack()
pila_episodio_v.push('Luke Skywalker')
pila_episodio_v.push('Han Solo')
pila_episodio_v.push('Chau')
pila_episodio_v.push('Leia Organa')
pila_episodio_v.push('Hola')
pila_episodio_v.push('Kylo Ren')
pila_episodio_v.push('Darth Vader')

pila_episodio_vii = Stack()
pila_episodio_vii.push('Rey')
pila_episodio_vii.push('Finn')
pila_episodio_vii.push('Leia Organa')
pila_episodio_vii.push('Han Solo')
pila_episodio_vii.push('Chau')
pila_episodio_vii.push('Kylo Ren')

interseccion = interseccion_pilas(pila_episodio_v, pila_episodio_vii)

print("Personajes en ambos episodios:")
while interseccion.size() > 0:
    print(interseccion.pop())

print("Personajes en pila de Episodio V:")
while pila_episodio_v.size() > 0:
    print(pila_episodio_v.pop())

print("Personajes en pila de Episodio VII:")
while pila_episodio_vii.size() > 0:
    print(pila_episodio_vii.pop())