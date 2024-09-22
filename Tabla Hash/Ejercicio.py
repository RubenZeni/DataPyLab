# Escribir un algoritmo que permita utilizar tres tablas hash para guardar los datos de Pokémons, que contemple las siguientes actividades: 


# A. En la primera tabla hash la función hash debe ser sobre el tipo de Pokémon, en la segunda tabla la función hash deberá utilizar el ultimo dígito del número del Pokémon como clave y la tercera sera en base a su nivel repartiéndolos en 10 posiciones dentro de la tabla.
# B. Debe utilizar tablas hash abiertas con listas como estructura secundaria.
# C. Si el Pokémon es de más de un tipo deberá cargarlo en cada uno de las tabla que indiquen estos tipos.
# D. Deberá permitir cargar Pokémons de los cuales se dispone de su número, nombre, tipo/s, nivel.
tabla_tipo = {}
tabla_digito = {}
tabla_nivel = {}
def agregar_pokemon(numero, nombre, nivel, tipos):
	# A. Agregar a la tabla por tipo:
	for tipo in tipos:
		if tipo not in tabla_tipo:
			tabla_tipo[tipo] = []
		tabla_tipo[tipo].append({"numero": numero, "nombre": nombre, "nivel": nivel})
	# B. Agregar a la tabla por último dígito del número:
	ultimo_digito = numero % 10
	if ultimo_digito not in tabla_digito:
		tabla_digito[ultimo_digito] = []
		tabla_digito[ultimo_digito].append({"numero": numero, "nombre": nombre, "nivel": nivel})
	# C. Agregar a la tbala por nivel (dividido en 10 rangos):
	rango_nivel = nivel // 10
	if rango_nivel not in tabla_nivel:
		tabla_nivel[rango_nivel] = []
		tabla_nivel[rango_nivel].append({"numero": numero, "nombre": nombre, "nivel": nivel})

pokemons = [
  {
	"numero": 9,
	"nombre": "Blastoise",
	"nivel": 50,
	"tipo": "Agua",
  },
  {
	"numero": 1,
	"nombre": "Bulbasaur",
	"nivel": 30,
	"tipo": "Planta",
  },
  {
	"numero": 6,
	"nombre": "Charizard",
	"nivel": 40,
	"tipo": "Fuego",
  },
  {
	"numero": 74,
	"nombre": "Geodude",
	"nivel": 28,
	"tipo": "Roca",
  },
  {
	"numero": 130,
	"nombre": "Gyarados",
	"nivel": 35,
	"tipo": "Agua",
  },
  {
	"numero": 34,
	"nombre": "Nidoking",
	"nivel": 40,
	"tipo": "Veneno",
  },
  {
	"numero": 95,
	"nombre": "Onix",
	"nivel": 38,
	"tipo": "Roca",
  },
  {
	"numero": 25,
	"nombre": "Pikachu",
	"nivel": 35,
	"tipo": "Eléctrico",
  },
  {
	"numero": 54,
	"nombre": "Psyduck",
	"nivel": 25,
	"tipo": "Agua",
  },
  {
	"numero": 121,
	"nombre": "Starmie",
	"nivel": 30,
	"tipo": "Agua",
  },
  {
	"numero": 197,
	"nombre": "Umbreon",
	"nivel": 45,
	"tipo": "Siniestro",
  },
  {
	"numero": 37,
	"nombre": "Vulpix",
	"nivel": 20,
	"tipo": "Fuego",
  }
]
for pokemon in pokemons:
	agregar_pokemon(pokemon["numero"], pokemon["nombre"], pokemon["nivel"], [pokemon["tipo"]])

print("A, B, C y D:")
print("* Tabla por tipo:", end = "\n  ")
for indice, tipo in enumerate(tabla_tipo):
	print(tipo, end = ", " if indice < len(tabla_tipo) - 2 else " y " if indice == len(tabla_tipo) - 2 else ".\n")
print("* Tabla por dígito:", end = "\n  ")
for indice, digito in enumerate(tabla_digito):
	print(digito, end = ", " if indice < len(tabla_digito) - 2 else " y " if indice == len(tabla_digito) - 2 else ".\n")
print("* Tabla por nivel:", end = "\n  ")
for indice, nivel in enumerate(tabla_nivel):
	print(nivel, end = ", " if indice < len(tabla_nivel) - 2 else " y " if indice == len(tabla_nivel) - 2 else ".\n")


# E. Mostrar todos los Pokémons cuyos numeros terminan en 3, 7 y 9.
print("\nE:")
print("Pokémons cuyos números terminan en 3, 7 y 9:")
for digito in [3, 7, 9]:
	if digito in tabla_digito:
		for pokemon in tabla_digito[digito]:
			print(f"Número: {pokemon["numero"]}, Nombre: {pokemon["nombre"]}, Nivel: {pokemon["nivel"]}.")


# F. Mostrar todos los Pokémons cuyos niveles son multiplos de 2, 5 y 10.
print("\nF:")
print("Pokémons cuyos niveles son múltiplos de 2, 5 y 10:")
for _, pokemones in tabla_nivel.items():
	for pokemon in pokemones:
		if pokemon["nivel"] % 2 == 0 or pokemon["nivel"] % 5 == 0 or pokemon["nivel"] % 10 == 0:
			print(f"Número: {pokemon["numero"]}, Nombre: {pokemon["nombre"]}, Nivel: {pokemon["nivel"]}.")


# G. Mostrar todos los Pokémons de los siguientes tipo: Acero, Fuego, Electrifico, Hielo.
print("\nG:")
print("Pokémons de tipo Acero, Fuego, Eléctrico y Hielo:")
for tipo in ["Acero", "Fuego", "Eléctrico", "Hielo"]:
	if tipo in tabla_tipo:
		for pokemon in tabla_tipo[tipo]:
			print(f"Número: {pokemon["numero"]}, Nombre: {pokemon["nombre"]}, Nivel: {pokemon["nivel"]}.")