# Código de resolución del ejercicio bajo el título ejercicio_grafo
from grafo import Graph

# Crear grafo no dirigido
grafo = Graph(dirigido=False)

# Agregar personajes y sus conexiones
personajes = ["Luke Skywalker", "Darth Vader", "Yoda", "Boba Fett", "C-3PO", "Leia", "Rey", "Kylo Ren", "Chewbacca", "Han Solo", "R2-D2", "BB-8"]
for personaje in personajes:
    grafo.insert_vertice(personaje)

# Establecer conexiones (aristas) entre personajes con el peso correspondiente a la cantidad de episodios compartidos
grafo.insert_arista("Luke Skywalker", "Darth Vader", 4)
grafo.insert_arista("Luke Skywalker", "Leia", 5)
grafo.insert_arista("Leia", "Darth Vader", 3)
grafo.insert_arista("Leia", "Han Solo", 4)
grafo.insert_arista("Luke Skywalker", "Yoda", 3)
grafo.insert_arista("Yoda", "Darth Vader", 2)
grafo.insert_arista("Chewbacca", "Han Solo", 6)
grafo.insert_arista("Rey", "Kylo Ren", 2)
grafo.insert_arista("Leia", "Rey", 1)
grafo.insert_arista("C-3PO", "R2-D2", 7)
grafo.insert_arista("BB-8", "R2-D2", 1)

# A. Cada vértice debe almacenar el nombre de un personaje, las aristas representan la cantidad de episodios en los que aparecieron juntos ambos personajes que se relacionan.
# Ya implementado en la construcción del grafo.

# B. Hallar el árbol de expansión minino y determinar si contiene a Yoda.
bosque_minimo, contiene_yoda = grafo.kruskal_modificado()
print(f"\nB:\nI. Árbol de Expansión Mínimo:") #\n{bosque_minimo}
for nodo in bosque_minimo:
    print(nodo)
print("II. ¿Contiene a Yoda?", "Sí" if contiene_yoda else "No")

# C. Determinar cuál es el número máximo de episodio que comparten dos personajes, y quienes son.
max_episodios, personajes = grafo.max_episodios_compartidos()
print("\nC:\nI. Máximo de episodios compartidos:", max_episodios)
print("II. Personajes que comparten el máximo de episodios:", personajes)

# D. Cargue al menos los siguientes personajes: Luke Skywalker, Darth Vader, Yoda, Boba Fett, C-3PO, Leia, Rey, Kylo Ren, Chewbacca, Han Solo, R2-D2, BB-8.
# Ya se ha realizado en los pasos previos.