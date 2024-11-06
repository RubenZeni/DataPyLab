from arbol_avl import ArbolBinario

# Implementar un algoritmo que permita generar un árbol con los datos de la siguiente tabla y resuelva las siguientes consultas:
# |-----------------------|----------------|--------------------|---------------|
# |Criaturas              | Derrotado por  | Criaturas          | Derrotado por |
# |-----------------------|----------------|--------------------|---------------|
# | Ceto                  | -              | Cerda de Cromión   | Teseo         |
# | Tifón                 | Zeus           | Ortro              | Heracles      |
# | Equidna               | Argos Panoptes | Toro de Creta      | Teseo         |
# | Dino                  | -              | Jabalí de Calidón  | Atalanta      |
# | Pefredo               | -              | Carcinos           | -             |
# | Enio                  | -              | Gerión             | Heracles      |
# | Escila                | -              | Cloto              | -             |
# | Caribdis              | -              | Láquesis           | -             |
# | Euríale               | -              | Átropos            | -             |
# | Esteno                | -              | Minotauro de Creta | Teseo         |
# | Medusa                | Perseo         | Harpías            | -             |
# | Ladón                 | Heracles       | Argos Panoptes     | Hermes        |
# | Águila del Cáucaso    | -              | Aves del Estínfalo | -             |
# | Quimera               | Belerofonte    | Talos              | Medea         |
# | Hidra de Lerna        | Heracles       | Sirenas            | -             |
# | León de Nemea         | Heracles       | Pitón              | Apolo         |
# | Esfinge               | Edipo          | Cierva de Cerinea  | -             |
# | Dragón de la Cólquida | -              | Basilisco          | -             |
# | Cerbero               | -              | Jabalí de Erimanto | -             |
# |-----------------------|----------------|--------------------|---------------|

criaturas = [
	{
		"nombre": "Ceto",
		"derrotada_por": None,
		"capturada_por": None,
		"descripcion": ""
	},
	{
		"nombre": "Tifón",
		"derrotada_por": "Zeus",
		"capturada_por": None,
		"descripcion": ""
	},
	{
		"nombre": "Equidna",
		"derrotada_por": "Argos Panoptes",
		"capturada_por": None,
		"descripcion": ""
	},
	{
		"nombre": "Dino",
		"derrotada_por": None,
		"capturada_por": None,
		"descripcion": ""
	},
	{
		"nombre": "Pefredo",
		"derrotada_por": None,
		"capturada_por": None,
		"descripcion": ""
	},
	{
		"nombre": "Enio",
		"derrotada_por": None,
		"capturada_por": None,
		"descripcion": ""
	},
	{
		"nombre": "Escila",
		"derrotada_por": None,
		"capturada_por": None,
		"descripcion": ""
	},
	{
		"nombre": "Caribdis",
		"derrotada_por": None,
		"capturada_por": None,
		"descripcion": ""
	},
	{
		"nombre": "Euríale",
		"derrotada_por": None,
		"capturada_por": None,
		"descripcion": ""
	},
	{
		"nombre": "Esteno",
		"derrotada_por": None,
		"capturada_por": None,
		"descripcion": ""
	},
	{
		"nombre": "Medusa",
		"derrotada_por": "Perseo",
		"capturada_por": None,
		"descripcion": ""
	},
	{
		"nombre": "Ladón",
		"derrotada_por": "Heracles",
		"capturada_por": None,
		"descripcion": ""
	},
	{
		"nombre": "Águila del Cáucaso",
		"derrotada_por": None,
		"capturada_por": None,
		"descripcion": ""
	},
	{
		"nombre": "Quimera",
		"derrotada_por": "Belerofonte",
		"capturada_por": None,
		"descripcion": ""
	},
	{
		"nombre": "Hidra de Lerna",
		"derrotada_por": "Heracles",
		"capturada_por": None,
		"descripcion": ""
	},
	{
		"nombre": "León de Nemea",
		"derrotada_por": "Heracles",
		"capturada_por": None,
		"descripcion": ""
	},
	{
		"nombre": "Esfinge",
		"derrotada_por": "Edipo",
		"capturada_por": None,
		"descripcion": ""
	},
	{
		"nombre": "Dragón de la Cólquida",
		"derrotada_por": None,
		"capturada_por": None,
		"descripcion": ""
	},
	{
		"nombre": "Cerbero",
		"derrotada_por": None,
		"capturada_por": None,
		"descripcion": ""
	},
	{
		"nombre": "Cerda de Cromión",
		"derrotada_por": "Teseo",
		"capturada_por": None,
		"descripcion": ""
	},
	{
		"nombre": "Ortro",
		"derrotada_por": "Heracles",
		"capturada_por": None,
		"descripcion": ""
	},
	{
		"nombre": "Toro de Creta",
		"derrotada_por": "Teseo",
		"capturada_por": None,
		"descripcion": ""
	},
	{
		"nombre": "Jabalí de Calidón",
		"derrotada_por": "Atalanta",
		"capturada_por": None,
		"descripcion": ""
	},
	{
		"nombre": "Carcinos",
		"derrotada_por": None,
		"capturada_por": None,
		"descripcion": ""
	},
	{
		"nombre": "Gerión",
		"derrotada_por": "Heracles",
		"capturada_por": None,
		"descripcion": ""
	},
	{
		"nombre": "Cloto",
		"derrotada_por": None,
		"capturada_por": None,
		"descripcion": ""
	},
	{
		"nombre": "Láquesis",
		"derrotada_por": None,
		"capturada_por": None,
		"descripcion": ""
	},
	{
		"nombre": "Átropos",
		"derrotada_por": None,
		"capturada_por": None,
		"descripcion": ""
	},
	{
		"nombre": "Minotauro de Creta",
		"derrotada_por": "Teseo",
		"capturada_por": None,
		"descripcion": ""
	},
	{
		"nombre": "Harpías",
		"derrotada_por": None,
		"capturada_por": None,
		"descripcion": ""
	},
	{
		"nombre": "Argos Panoptes",
		"derrotada_por": "Hermes",
		"capturada_por": None,
		"descripcion": ""
	},
	{
		"nombre": "Aves del Estínfalo",
		"derrotada_por": None,
		"capturada_por": None,
		"descripcion": ""
	},
	{
		"nombre": "Talos",
		"derrotada_por": "Medea",
		"capturada_por": None,
		"descripcion": ""
	},
	{
		"nombre": "Sirenas",
		"derrotada_por": None,
		"capturada_por": None,
		"descripcion": ""
	},
	{
		"nombre": "Pitón",
		"derrotada_por": "Apolo",
		"capturada_por": None,
		"descripcion": ""
	},
	{
		"nombre": "Cierva de Cerinea",
		"derrotada_por": None,
		"capturada_por": None,
		"descripcion": ""
	},
	{
		"nombre": "Basilisco",
		"derrotada_por": None,
		"capturada_por": None,
		"descripcion": ""
	},
	{
		"nombre": "Jabalí de Erimanto",
		"derrotada_por": None,
		"capturada_por": None,
		"descripcion": ""
	},
]

arbol_criaturas = ArbolBinario()
for criatura in criaturas:
	arbol_criaturas.insertar_nodo(criatura["nombre"], {"derrotada_por": criatura["derrotada_por"], "descripcion": criatura["descripcion"]})

# A. Listado inorden de las criaturas y quienes la derrotaron.
print("A:\n|-------------------------|------------------|")
print("| Criatura                | Derrotada por    |")
print("|-------------------------|------------------|")
arbol_criaturas.inorden_criaturas()
print("|-------------------------|------------------|")

# B. Se debe permitir cargar una breve descripción sobre cada criatura.
print("\nB:")
arbol_criaturas.insertar_descripcion("Basilisco", "Serpiente mítica que mata con su mirada, símbolo del peligro y la muerte.")
arbol_criaturas.insertar_descripcion("Talos", "Autómata de bronce que protegía Creta, conocido por su fuerza y lealtad.")
# arbol_criaturas.insertar_descripcion(input("Criatura: "), input("Descripción: "))

# C. Mostrar toda la información de la criatura Talos.
print("\nC:")
arbol_criaturas.mostrar_informacion("Talos")

# D. Determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas.
print("\nD:")
top_3_heroes_dioses = arbol_criaturas.top_3_heroes_dioses()
top_3_heroes_dioses = list(top_3_heroes_dioses.items())
heroes_dioses = []
heroes_dioses += ([[indice, nombre] for indice, (nombre, cantidad) in enumerate(top_3_heroes_dioses) if cantidad == max([cantidad for nombre, cantidad in top_3_heroes_dioses])])
top_3_heroes_dioses.pop(heroes_dioses[0][0])
heroes_dioses += ([[indice, nombre] for indice, (nombre, cantidad) in enumerate(top_3_heroes_dioses) if cantidad == max([cantidad for nombre, cantidad in top_3_heroes_dioses])])
top_3_heroes_dioses.pop(heroes_dioses[1][0])
heroes_dioses += ([[indice, nombre] for indice, (nombre, cantidad) in enumerate(top_3_heroes_dioses) if cantidad == max([cantidad for nombre, cantidad in top_3_heroes_dioses])])
top_3_heroes_dioses.pop(heroes_dioses[2][0])
print(f"Los 3 héroes o dioses que derrotaron mayor cantidad de criaturas son {heroes_dioses[0][1]}, {heroes_dioses[1][1]} y {heroes_dioses[2][1]}.")

# E. Listar las criaturas derrotadas por Heracles.
print(f"\nE:\nHeracles derrotó a un total de {arbol_criaturas.cantidad_derrotadas_por("Heracles")} criaturas.")

# F. Listar las criaturas que no han sido derrotadas.
print("\nF:\nCriaturas que no han sido derrotadas:")
criaturas_no_derrotadas = arbol_criaturas.criaturas_no_derrotadas()
for criatura in criaturas_no_derrotadas:
	print(criatura)

# G. Además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe o dios que la capturo.
for criatura in criaturas:
	arbol_criaturas.agregar_modificar_campo(criatura["nombre"], "capturada", criatura["capturada_por"])

# H. Modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva de Cerinea y Jabalí de Erimanto indicando que Heracles las atrapó.
print("\nH:")
capturadas = ["Cerbero", "Toro de Creta", "Cierva de Cerinea", "Jabalí de Erimanto"]
for captura in capturadas:
	arbol_criaturas.registrar_captura(captura, "Heracles")

# I. Se debe permitir búsquedas por coincidencia.
print("\nI:\nBúsquedas de ejemplo:")
print("\n'Creta':")
nodos = arbol_criaturas.busqueda_por_coincidencia("Creta")
for raiz in nodos:
	print(raiz.valor)
print("\n'del':")
nodos = arbol_criaturas.busqueda_por_coincidencia("del")
for raiz in nodos:
	print(raiz.valor)

# J. Eliminar al Basilisco y a las Sirenas.
arbol_criaturas.eliminar_nodo("Basilisco")
arbol_criaturas.eliminar_nodo("Sirenas")

# K. Modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles derroto a varias.
print("\nK:")
arbol_criaturas.registrar_derrota("Aves del Estínfalo", "Heracles")

# L. Modifique el nombre de la criatura Ladón por Dragón Ladón.
print("\nL:")
arbol_criaturas.modificar_nombre_criatura("Ladón", "Dragón Ladón")

# M. Realizar un listado por nivel del árbol.
print("\nM:")
arbol_criaturas.por_nivel()

# N. Muestre las criaturas capturadas por Heracles.
print("\nN:")
criaturas = arbol_criaturas.criaturas_capturadas_por("Heracles")
for criatura in criaturas:
	print(criatura)