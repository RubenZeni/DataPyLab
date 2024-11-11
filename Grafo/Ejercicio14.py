# 14. Implementar sobre un grafo no dirigido los algoritmos necesario para dar solución a las siguientes tareas:

from grafo import Grafo

# se crea el grafo no dirigido

grafo_casa = Grafo(dirigido=False)

# A. Cada vértice representar un ambiente de una casa: cocina, comedor, cochera, quincho, baño 1, baño 2, habitación 1, habitación 2, sala de estar, terraza, patio.

ambientes = ["cocina", "comedor", "cochera", "quincho", "baño 1", "baño 2", "habitación 1", "habitación 2", "sala de estar", "terraza", "patio"]

for ambiente in ambientes:
	grafo_casa.insertar_vertice(ambiente)

# B. Cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco, el peso de la arista es la distancia entre los ambientes, se debe cargar en metros.

grafo_casa.insertar_arista("cocina", "comedor", 5)
grafo_casa.insertar_arista("cocina", "baño 1", 10)
grafo_casa.insertar_arista("cocina", "terraza", 15)

grafo_casa.insertar_arista("comedor", "cocina", 5)
grafo_casa.insertar_arista("comedor", "sala de estar", 7)
grafo_casa.insertar_arista("comedor", "patio", 12)

grafo_casa.insertar_arista("cochera", "quincho", 20)
grafo_casa.insertar_arista("cochera", "habitación 1", 25)
grafo_casa.insertar_arista("cochera", "comedor", 18)

grafo_casa.insertar_arista("quincho", "terraza", 8)
grafo_casa.insertar_arista("quincho", "patio", 10)
grafo_casa.insertar_arista("quincho", "baño 2", 15)

grafo_casa.insertar_arista("baño 1", "habitación 1", 5)
grafo_casa.insertar_arista("baño 1", "baño 2", 6)
grafo_casa.insertar_arista("baño 1", "cocina", 10)

grafo_casa.insertar_arista("baño 2", "habitación 2", 4)
grafo_casa.insertar_arista("baño 2", "quincho", 15)
grafo_casa.insertar_arista("baño 2", "terraza", 12)

grafo_casa.insertar_arista("habitación 1", "habitación 2", 3)
grafo_casa.insertar_arista("habitación 1", "baño 1", 5)
grafo_casa.insertar_arista("habitación 1", "sala de estar", 8)

grafo_casa.insertar_arista("habitación 2", "baño 2", 4)
grafo_casa.insertar_arista("habitación 2", "habitación 1", 3)
grafo_casa.insertar_arista("habitación 2", "terraza", 9)

grafo_casa.insertar_arista("sala de estar", "comedor", 7)
grafo_casa.insertar_arista("sala de estar", "habitación 1", 8)
grafo_casa.insertar_arista("sala de estar", "terraza", 11)

grafo_casa.insertar_arista("terraza", "patio", 6)
grafo_casa.insertar_arista("terraza", "baño 2", 12)
grafo_casa.insertar_arista("terraza", "sala de estar", 11)

grafo_casa.insertar_arista("patio", "terraza", 6)
grafo_casa.insertar_arista("patio", "comedor", 12)
grafo_casa.insertar_arista("patio", "quincho", 10)

# C. Obtener el árbol de expansión mínima y determine cuantos metros de cables se necesitan para conectar todos los ambientes.
print("C.")
arbol_expansion_minima = grafo_casa.kruskal("cocina")
distancia_total_mst = 0
for arista in arbol_expansion_minima[0].split(';'):
	if '-' in arista:
		peso = int(arista.split('-')[-1])
		distancia_total_mst += peso
print("Para conectar todos los ambientes se necesitan en total de", distancia_total_mst, "metros de cables.\nArbol de expansion minima:")
for nodo in arbol_expansion_minima:
	print("------------------------------------------------------------------------------------------")
	print(nodo.replace("-", " - ").replace(";", " | "))
print("------------------------------------------------------------------------------------------")

# D. Determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para determinar cuántos metros de cable de red se necesitan para conectar el router con el Smart Tv.
print("\nD.")
camino_mas_corto = grafo_casa.dijkstra("habitación 1")
distancia_total = 0
while True:
	nodo = camino_mas_corto.desapilar()
	if nodo is None:
		break
	if nodo[1][0] == "sala de estar":
		distancia_total = nodo[0]
		break
print("Desde la habitación 1 hasta la sala de estar hay un total de", distancia_total, "metros de distancia.")