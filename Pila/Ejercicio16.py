'''Se tienen dos pilas con personajes de Star Wars, en una los del episodio V de “The empire strikes back” y la otra los del episodio VII “The force awakens”. Desarrollar un algoritmo que permita obtener la intersección de ambas pilas, es decir los personajes que aparecen en ambos episodios.'''

from pila import Stack

def interseccion_pilas_sin_set(pila1, pila2):
    auxiliar1 = Stack()
    auxiliar2 = Stack()
    interseccion = Stack()

    while pila1.size() > 0:
        elemento = pila1.pop()
        auxiliar1.push(elemento)
    
    while pila2.size() > 0:
        elemento = pila2.pop()
        
        esta_en_pila1 = False
        while auxiliar1.size() > 0:
            aux_elemento = auxiliar1.pop()
            auxiliar2.push(aux_elemento)
            if aux_elemento == elemento:
                esta_en_pila1 = True
        
        while auxiliar2.size() > 0:
            auxiliar1.push(auxiliar2.pop())
        
        if esta_en_pila1:
            interseccion.push(elemento)
    
    while interseccion.size() > 0:
        elemento = interseccion.pop()
        pila2.push(elemento)
        pila1.push(elemento)
    
    return interseccion

pila_episodio_v = Stack()
pila_episodio_v.push('Luke Skywalker')
pila_episodio_v.push('Han Solo')
pila_episodio_v.push('Leia Organa')
pila_episodio_v.push('Darth Vader')

pila_episodio_vii = Stack()
pila_episodio_vii.push('Rey')
pila_episodio_vii.push('Finn')
pila_episodio_vii.push('Leia Organa')
pila_episodio_vii.push('Han Solo')
pila_episodio_vii.push('Kylo Ren')

interseccion = interseccion_pilas_sin_set(pila_episodio_v, pila_episodio_vii)

print("Personajes en ambos episodios:")
while interseccion.size() > 0:
    print(interseccion.pop())