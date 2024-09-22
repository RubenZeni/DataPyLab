# Se cuenta con una lista de entrenadores Pokémon. De cada uno de estos se conoce: nombre, cantidad de torneos ganados, cantidad de batallas perdidas y cantidad de batallas ganadas. Y además la lista de sus Pokémons, de los cuales se sabe: nombre, nivel, tipo y subtipo. Se pide resolver las siguientes actividades utilizando lista de lista implementando las funciones necesarias:
from random import randint, sample

entrenadores = [
  {
	"nombre": "Ash Ketchum",
	"torneos_ganados": 7,
	"batallas_perdidas": 50,
	"batallas_ganadas": 120
  },
  {
	"nombre": "Goh",
	"torneos_ganados": 2,
	"batallas_perdidas": 10,
	"batallas_ganadas": 40
  },
  {
	"nombre": "Leon",
	"torneos_ganados": 10,
	"batallas_perdidas": 5,
	"batallas_ganadas": 100
  },
  {
	"nombre": "Chloe",
	"torneos_ganados": 1,
	"batallas_perdidas": 8,
	"batallas_ganadas": 30
  },
  {  
	"nombre": "Raihan",
	"torneos_ganados": 4,
	"batallas_perdidas": 15,
	"batallas_ganadas": 60
  }
]

pokemons = [
  {
	"nombre": "Pikachu",
	"nivel": 35,
	"tipo": "Eléctrico",
	"subtipo": None
  },
  {
	"nombre": "Charizard",
	"nivel": 40,
	"tipo": "Fuego",
	"subtipo": "Volador"
  },
  {
	"nombre": "Bulbasaur",
	"nivel": 30,
	"tipo": "Planta",
	"subtipo": "Veneno"
  },
  {
	"nombre": "Starmie",
	"nivel": 30,
	"tipo": "Agua",
	"subtipo": "Psíquico"
  },
  {
	"nombre": "Psyduck",
	"nivel": 25,
	"tipo": "Agua",
	"subtipo": None
  },
  {
	"nombre": "Gyarados",
	"nivel": 35,
	"tipo": "Agua",
	"subtipo": "Volador"
  },
  {
	"nombre": "Onix",
	"nivel": 38,
	"tipo": "Roca",
	"subtipo": "Tierra"
  },
  {
	"nombre": "Geodude",
	"nivel": 28,
	"tipo": "Roca",
	"subtipo": "Tierra"
  },
  {
	"nombre": "Vulpix",
	"nivel": 20,
	"tipo": "Fuego",
	"subtipo": None
  },
  {
	"nombre": "Blastoise",
	"nivel": 50,
	"tipo": "Agua",
	"subtipo": None
  },
  {
	"nombre": "Umbreon",
	"nivel": 45,
	"tipo": "Siniestro",
	"subtipo": None
  },
  {
	"nombre": "Nidoking",
	"nivel": 40,
	"tipo": "Veneno",
	"subtipo": "Tierra"
  }
]


def search(lista, criterio, valor):
	for indice, elemento in enumerate(lista):
		if elemento[criterio] == valor:
			return indice

def remove(lista, criterio, valor):
	indice = search(lista, criterio, valor)
	if indice is not None:
		return lista.pop(indice)

def ordenar(lista, criterio, reverse = False): #Defino esta función para no tener que definir más funciones by_criterio
	lista.sort(key = lambda item: item[criterio], reverse = reverse)

def barrido_continuo(lista):
	cadena = ""
	for indice, elemento in enumerate(lista):
		cadena += elemento + (", " if indice < len(lista) - 2 else " y " if indice == len(lista) - 2 else "")
	return cadena

def cantidad_pokemons(entrenadores, entrenador):
	indice = search(entrenadores, "nombre", entrenador)
	if indice is not None:
		return len(entrenadores[indice]["pokemons"])

def datos_entrenador_pokemons(entrenadores, nombre):
	indice = search(entrenadores, "nombre", nombre)
	if indice is not None:
		entrenador = entrenadores[indice]
		print(f"Nombre: {entrenador["nombre"]}")
		print(f"Torneos ganados: {entrenador["torneos_ganados"]}")
		print(f"Batallas perdidas: {entrenador["batallas_perdidas"]}")
		print(f"Batallas ganadas: {entrenador["batallas_ganadas"]}")
		print("Pokemons:" if len(entrenador["pokemons"]) > 1 else "Pokemon:")
		for index, pokemon in enumerate(entrenador["pokemons"]):
			print(f"{index + 1}. Nombre: {pokemon["nombre"]}")
			print("   Nivel:", pokemon["nivel"])
			print("   Tipo:", pokemon["tipo"])
			print("   Subtipo:", pokemon["subtipo"])

def promedio_nivel_pokemons(entrenadores, entrenador):
	indice = search(entrenadores, "nombre", entrenador)
	if indice is not None:
		nivel_total = 0
		for pokemon in entrenadores[indice]["pokemons"]:
			nivel_total += pokemon["nivel"]
		return (nivel_total // len(entrenadores[indice]["pokemons"]))

def poseedores_pokemon(entrenadores, pokemon):
	poseedores = []
	for entrenador in entrenadores:
		pokemons_entrenador = [pokemon["nombre"] for pokemon in entrenador["pokemons"]]
		if pokemon in pokemons_entrenador:
			poseedores.append(entrenador["nombre"])
	return poseedores

# Agregar lo pokemons del ejercicio J (línea 287) a la lista:
pokemons = pokemons + [
  {
	"nombre": "Tyrantrum",
	"nivel": 30,
	"tipo": "Roca",
	"subtipo": "Dragón"
  },
  {
	"nombre": "Terrakion",
	"nivel": 20,
	"tipo": "Roca",
	"subtipo": "Lucha"
  },
  {
	"nombre": "Wingull",
	"nivel": 25,
	"tipo": "Agua",
	"subtipo": "Volador"
  }
]

# Agregar pokemons a los entrenadores (ordenados alfabéticamente):
for entrenador in entrenadores:
	pokemons_aleatorios = sample(pokemons, randint(1, 5))
	ordenar(pokemons_aleatorios, "nombre")
	entrenador["pokemons"] = pokemons_aleatorios

from Lista import mostrar_lista_sublista
mostrar_lista_sublista(entrenadores, "nombre", "Entrenadores", "pokemons", "Pokemons")


# A. Obtener la cantidad de Pokémons de un determinado entrenador.
print("A:")
entrenador = "Chloe"
# entrenador = input("Entrenador: ")
cantidad = cantidad_pokemons(entrenadores, entrenador)
if cantidad is not None:
	print(entrenador, "posee", cantidad, "pokemon." if cantidad == 1 else "pokemons.")
else:
	print(entrenador, "no posee pokemons.")


# B. Listar los entrenadores que hayan ganado más de tres torneos.
print("\nB:")
ganadores = [entrenador["nombre"] for entrenador in entrenadores if entrenador["torneos_ganados"] > 3]
print(f"Los entrenadores que han ganado más de 3 torneos son {barrido_continuo(ganadores)}.")


# C. El Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados.
print("\nC:")
max_entrenador = max(entrenadores, key = lambda entrenador: entrenador["torneos_ganados"])
max_pokemon = max(max_entrenador["pokemons"], key = lambda pokemon: pokemon["nivel"])
print(f"El entenador con mayor cantidad de torneos ganados es {max_entrenador["nombre"]}, y su pokemon de mayor nivel es {max_pokemon["nombre"]}.")


# D. Mostrar todos los datos de un entrenador y sus Pokémons.
print("\nD:")
entrenador = "Chloe"
# entrenador = input("Entrenador: ")
datos_entrenador_pokemons(entrenadores, entrenador)


# E. Mostrar los entrenadores cuyo porcentaje de batallas ganadas sea mayor al 79 %. (CANTIDAD * 100 / TOTAL)
print("\nE:")
ganadores = []
for entrenador in entrenadores:
	porcentaje_ganadas = (entrenador["batallas_ganadas"] * 100) / (entrenador["batallas_ganadas"] + entrenador["batallas_perdidas"])
	if porcentaje_ganadas > 79:
		ganadores.append(entrenador["nombre"])
print(f"Entrenadores cuyo porcentaje de batallas ganadas es mayor al 79%: {barrido_continuo(ganadores)}.")


# F. Los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador (tipo y subtipo)
print("\nF:")
pokemons_elegidos = []
entrenadores_elegidos = []
for pokemon in pokemons:
	if pokemon["tipo"] is not None and pokemon["nombre"] not in pokemons_elegidos:
		if pokemon["tipo"] == "Fuego" or pokemon["tipo"] == "Planta":
			pokemons_elegidos.append(pokemon)
		elif pokemon["tipo"] == "Agua" and pokemon["subtipo"] is not None:
			if pokemon["subtipo"] == "Volador":
				pokemons_elegidos.append(pokemon)
print("Los pokemons tipo Fuego y Planta o Agua/Volador son: ", end = "")
for indice, pokemon in enumerate(pokemons_elegidos):
	print(pokemon["nombre"], f"(tipo {pokemon["tipo"]} y subtipo {pokemon["subtipo"]})" if pokemon["tipo"] == "Agua" else f"(tipo {pokemon["tipo"]})", end = ", " if indice < len(pokemons_elegidos) - 2 else " y " if indice == len(pokemons_elegidos) - 2 else ".\n")
pokemons_elegidos = [pokemon["nombre"] for pokemon in pokemons_elegidos]
for entrenador in entrenadores:
	for pokemon in entrenador["pokemons"]:
		if pokemon["nombre"] in pokemons_elegidos:
			entrenadores_elegidos.append(entrenador["nombre"])
			break
print(f"Los entrenadores que tienen al menos uno de estos pokemons son {barrido_continuo(entrenadores_elegidos)}.")


# G. El promedio de nivel de los Pokémons de un determinado entrenador
print("\nG:")
entrenador = "Chloe"
# entrenador = input("Entrenador: ")
print(f"El promedio de nivel de los pokemons de {entrenador} es de {promedio_nivel_pokemons(entrenadores, entrenador)}.")


# H. Determinar cuántos entrenadores tienen a un determinado Pokémon.
print("\nH:")
pokemon = "Pikachu"
# pokemon = input("Pokemon: ")
poseedores = poseedores_pokemon(entrenadores, pokemon)
if poseedores:
	print(f"Sólo {barrido_continuo(poseedores)} posee a {pokemon}." if len(poseedores) == 1 else f"{barrido_continuo(poseedores)} poseen a {pokemon}.")
else:
	print(f"Ningún entrenador posee a {pokemon}.")


# I. Mostrar los entrenadores que tienen Pokémons repetidos.
print("\nI:")
repetidos = set()
lista = ""
for indice, entrenador_out in enumerate(entrenadores):
	pokemons_entrenador_out = [pokemon["nombre"] for pokemon in entrenador_out["pokemons"]]
	if indice < len(entrenadores) - 1:
		for entrenador_in in entrenadores[indice + 1:]:
			for pokemon in entrenador_in["pokemons"]:
				if pokemon["nombre"] in pokemons_entrenador_out:
					lista = lista + f"{entrenador_out["nombre"]} y {entrenador_in["nombre"]} tienen a {pokemon["nombre"]}.\n"
					repetidos.add(entrenador_out["nombre"])
print(f"Los entrenadores que tienen pokemons repetidos son {barrido_continuo(repetidos)}:\n{lista}")


# J. Determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion o Wingull.
print("\nJ:")
lista = ["Tyrantrum", "Terrakion", "Wingull"]
for entrenador in entrenadores:
	pokemons_entrenador = [pokemon["nombre"] for pokemon in entrenador["pokemons"] if pokemon["nombre"] in lista]
	if pokemons_entrenador:
		
		print(f"{entrenador["nombre"]} tiene a {barrido_continuo(pokemons_entrenador)}.")


# K. Determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se deberán mostrar los datos de ambos.
print("\nK:")
# X = "Chloe"
X = input("Entrenador: ")
# Y = "Pickachu"
Y = input("Pokemon: ")
indice_entrenador = search(entrenadores, "nombre", X)
if indice_entrenador is not None:
	indice_pokemon = search(entrenadores[indice_entrenador]["pokemons"], "nombre", Y)
	if indice_pokemon is not None:
		print(f"\n{X} tiene {Y}. Datos de ambos:")
		print(f"{X}:")
		print("Torneos ganados:", entrenadores[indice_entrenador]["torneos_ganados"])
		print("Batallas ganadas:", entrenadores[indice_entrenador]["batallas_ganadas"])
		print("Batallas perdidas:", entrenadores[indice_entrenador]["batallas_perdidas"])
		print(f"{Y}:")
		print("   Nivel:", entrenadores[indice_entrenador]["pokemons"][indice_pokemon]["nivel"])
		print("   Tipo:", entrenadores[indice_entrenador]["pokemons"][indice_pokemon]["tipo"])
		print("   Subtipo:", entrenadores[indice_entrenador]["pokemons"][indice_pokemon]["subtipo"])
	else:
		print(f"\n{X} no tiene a {Y}")
else:
	print(f"\n{X} no existe en la lista de entrenadores.")