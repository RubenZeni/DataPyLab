# 15. Se requiere implementar un grafo para almacenar las siete maravillas arquitectónicas modernas y naturales del mundo, para lo cual se deben tener en cuenta las siguientes actividades:

from grafo import Grafo
# F. Deberá utilizar un grafo no dirigido.
grafo_maravillas = Grafo(dirigido=False)

# A. De cada una de las maravillas se conoce su nombre, país de ubicación (puede ser más de uno en las naturales) y tipo (natural o arquitectónica).
maravillas = [
	{"nombre": "Chichen Itza", "pais": ["México"], "tipo": "arquitectónica"},
	{"nombre": "Cristo Redentor", "pais": ["Brasil"], "tipo": "arquitectónica"},
	{"nombre": "Machu Picchu", "pais": ["Perú"], "tipo": "arquitectónica"},
	{"nombre": "Coliseo", "pais": ["Italia"], "tipo": "arquitectónica"},
	{"nombre": "Taj Mahal", "pais": ["India"], "tipo": "arquitectónica"},
	{"nombre": "Petra", "pais": ["Jordania"], "tipo": "arquitectónica"},
	{"nombre": "Gran Muralla China", "pais": ["China"], "tipo": "arquitectónica"},
	{"nombre": "Amazonas", "pais": ["Brasil", "Perú", "Colombia"], "tipo": "natural"},
	{"nombre": "Bahía de Ha Long", "pais": ["Vietnam"], "tipo": "natural"},
	{"nombre": "Cataratas del Iguazú", "pais": ["Argentina", "Brasil"], "tipo": "natural"},
	{"nombre": "Isla Jeju", "pais": ["Corea del Sur"], "tipo": "natural"},
	{"nombre": "Komodo", "pais": ["Indonesia"], "tipo": "natural"},
	{"nombre": "Parque Nacional de las Montañas Azules", "pais": ["Australia"], "tipo": "natural"},
	{"nombre": "Table Mountain", "pais": ["Sudáfrica"], "tipo": "natural"}
]

# Agregamos las maravillas como vértices en el grafo
for maravilla in maravillas:
	grafo_maravillas.insertar_vertice(maravilla["nombre"])

# B. Cada una debe estar relacionada con las otras seis de su tipo, para lo que se debe almacenar la distancia que las separa.
# Suponiendo una lista de distancias entre maravillas de cada tipo
distancias_arquitectonicas = [
	("Chichen Itza", "Cristo Redentor", 2000),
	("Chichen Itza", "Machu Picchu", 4000),
	("Chichen Itza", "Coliseo", 8000),
	("Chichen Itza", "Taj Mahal", 15000),
	("Chichen Itza", "Petra", 13000),
	("Chichen Itza", "Gran Muralla China", 12000),
	("Cristo Redentor", "Machu Picchu", 3500),
	("Cristo Redentor", "Coliseo", 9400),
	("Cristo Redentor", "Taj Mahal", 13900),
	("Cristo Redentor", "Petra", 11100),
	("Cristo Redentor", "Gran Muralla China", 17500),
	("Machu Picchu", "Coliseo", 10700),
	("Machu Picchu", "Taj Mahal", 15000),
	("Machu Picchu", "Petra", 14500),
	("Machu Picchu", "Gran Muralla China", 16500),
	("Coliseo", "Taj Mahal", 6700),
	("Coliseo", "Petra", 2500),
	("Coliseo", "Gran Muralla China", 8000),
	("Taj Mahal", "Petra", 4300),
	("Taj Mahal", "Gran Muralla China", 5000),
	("Petra", "Gran Muralla China", 4900),
]

distancias_naturales = [
	("Amazonas", "Bahía de Ha Long", 17000),
	("Amazonas", "Cataratas del Iguazú", 3200),
	("Amazonas", "Isla Jeju", 18000),
	("Amazonas", "Komodo", 19000),
	("Amazonas", "Parque Nacional de las Montañas Azules", 13000),
	("Amazonas", "Table Mountain", 14000),
	("Bahía de Ha Long", "Cataratas del Iguazú", 20000),
	("Bahía de Ha Long", "Isla Jeju", 2700),
	("Bahía de Ha Long", "Komodo", 4000),
	("Bahía de Ha Long", "Parque Nacional de las Montañas Azules", 7600),
	("Bahía de Ha Long", "Table Mountain", 13000),
	("Cataratas del Iguazú", "Isla Jeju", 20000),
	("Cataratas del Iguazú", "Komodo", 19000),
	("Cataratas del Iguazú", "Parque Nacional de las Montañas Azules", 13500),
	("Cataratas del Iguazú", "Table Mountain", 16000),
	("Isla Jeju", "Komodo", 4800),
	("Isla Jeju", "Parque Nacional de las Montañas Azules", 8600),
	("Isla Jeju", "Table Mountain", 13400),
	("Komodo", "Parque Nacional de las Montañas Azules", 5800),
	("Komodo", "Table Mountain", 10600),
	("Parque Nacional de las Montañas Azules", "Table Mountain", 11000),
]

# Se agregan las aristas en el grafo
for origen, destino, distancia in distancias_arquitectonicas + distancias_naturales:
	grafo_maravillas.insertar_arista(origen, destino, distancia)

# C. Hallar el árbol de expansión mínimo de cada tipo de las maravillas.
def arbol_minimo_por_tipo(tipo):
	vertices_tipo = [vertice for vertice in maravillas if vertice["tipo"] == tipo]
	return grafo_maravillas.kruskal(vertices_tipo[0]["nombre"])

arbol_minimo_arquitectonico = arbol_minimo_por_tipo("arquitectónica")
arbol_minimo_natural = arbol_minimo_por_tipo("natural")

# D. Determinar si existen países que dispongan de maravillas arquitectónicas y naturales.
paises_arquitectonicos = {pais for m in maravillas if m["tipo"] == "arquitectónica" for pais in m["pais"]}
paises_naturales = {pais for m in maravillas if m["tipo"] == "natural" for pais in m["pais"]}
paises_con_ambos_tipos = paises_arquitectonicos.intersection(paises_naturales)

# E. Determinar si algún país tiene más de una maravilla del mismo tipo.
def paises_con_multiples_maravillas(tipo):
	contador = {}
	for m in maravillas:
		if m["tipo"] == tipo:
			for pais in m["pais"]:
				if pais in contador:
					contador[pais] += 1
				else:
					contador[pais] = 1
	return [pais for pais, count in contador.items() if count > 1]

paises_multiples_arquitectonicas = paises_con_multiples_maravillas("arquitectónica")
paises_multiples_naturales = paises_con_multiples_maravillas("natural")

print("C.I.\nÁrbol de expansión mínima arquitectónico:")
for nodo in arbol_minimo_arquitectonico:
	print("------------------------------------------------------------------------------------------")
	print(nodo.replace("-", " - ").replace(";", " | "))
print("------------------------------------------------------------------------------------------")
print("\nC.II.\nÁrbol de expansión mínima natural:")
for nodo in arbol_minimo_natural:
	print("------------------------------------------------------------------------------------------")
	print(nodo.replace("-", " - ").replace(";", " | "))
print("------------------------------------------------------------------------------------------")
print("\nD.I.\nPaíses con múltiples maravillas arquitectónicas:")
for pais in paises_multiples_arquitectonicas:
	print(pais)
print("\nD.II.\nPaíses con múltiples maravillas naturales:")
for pais in paises_multiples_naturales:
	print(pais)
print("\nE.\nPaíses con maravillas de ambos tipos:")
for pais in paises_con_ambos_tipos:
	print(pais)