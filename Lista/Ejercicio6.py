# Dada una lista de superhéroes de comics, de los cuales se conoce su nombre, año aparición, casa de comic a la que pertenece (Marvel o DC) y biografía, implementar la funciones necesarias para poder realizar las siguientes actividades:
superheroes = [
  {
	"nombre": "Linterna Verde",
	"año_aparicion": 1940,
	"casa_comic": "DC Comics",
	"biografia": "Miembro de la Tropa de Linternas Verdes, posee un anillo que le otorga poderes basados en la fuerza de voluntad."
  },
  {
	"nombre": "Wolverine",
	"año_aparicion": 1974,
	"casa_comic": "Marvel Comics",
	"biografia": "Mutante con garras retráctiles y habilidades regenerativas, miembro de los X-Men."
  },
  {
	"nombre": "Doctor Strange",
	"año_aparicion": 1963,
	"casa_comic": "Marvel Comics",
	"biografia": "Hechicero supremo del universo Marvel, maestro de las artes místicas y protector de la realidad."
  },
  {
	"nombre": "Capitana Marvel",
	"año_aparicion": 1968,
	"casa_comic": "Marvel Comics",
	"biografia": "Heroína cósmica con poderes de vuelo, fuerza sobrehumana y energía cósmica."
  },
  {
	"nombre": "Mujer Maravilla",
	"año_aparicion": 1941,
	"casa_comic": "DC Comics",
	"biografia": "Princesa amazona y una de las principales defensoras de la justicia y la igualdad en el Universo DC."
  },
  {
	"nombre": "Flash",
	"año_aparicion": 1940,
	"casa_comic": "DC Comics",
	"biografia": "Velocista con la capacidad de correr a velocidades superiores a la luz, miembro de la Liga de la Justicia."
  },
  {
	"nombre": "Star-Lord",
	"año_aparicion": 1976,
	"casa_comic": "Marvel Comics",
	"biografia": "Líder de los Guardianes de la Galaxia, experto en combate y estrategia intergaláctica."
  },
  {
	"nombre": "Superman",
	"año_aparicion": 1938,
	"casa_comic": "DC Comics",
	"biografia": "El Hombre de Acero, uno de los héroes más icónicos de DC con superpoderes sobrehumanos."
  },
  {
	"nombre": "Batman",
	"año_aparicion": 1939,
	"casa_comic": "DC Comics",
	"biografia": "El Caballero Oscuro, detective y luchador experto que protege Gotham City."
  },
  {
	"nombre": "Iron Man",
	"año_aparicion": 1963,
	"casa_comic": "Marvel Comics",
	"biografia": "Tony Stark, genio multimillonario y superhéroe con una armadura tecnológica de alta tecnología."
  },
  {
	"nombre": "Wonder Woman",
	"año_aparicion": 1941,
	"casa_comic": "DC Comics",
	"biografia": "La princesa amazona Diana, guerrera y defensora de la paz y la justicia en el mundo."
  },
  {
	"nombre": "Spider-Man",
	"año_aparicion": 1962,
	"casa_comic": "Marvel Comics",
	"biografia": "Peter Parker, joven héroe con habilidades arácnidas tras ser picado por una araña radiactiva."
  },
  {
	"nombre": "Thor",
	"año_aparicion": 1962,
	"casa_comic": "Marvel Comics",
	"biografia": "Dios nórdico del trueno y miembro de los Vengadores, posee un martillo encantado llamado Mjolnir."
  },
  {
	"nombre": "Aquaman",
	"año_aparicion": 1941,
	"casa_comic": "DC Comics",
	"biografia": "Rey de Atlantis con la capacidad de comunicarse con la vida marina y controlar el agua."
  },
  {
	"nombre": "Green Arrow",
	"año_aparicion": 1941,
	"casa_comic": "DC Comics",
	"biografia": "Oliver Queen, arquero habilidoso y defensor de la justicia con su arco y flechas."
  },
  {
	"nombre": "Hulk",
	"año_aparicion": 1962,
	"casa_comic": "Marvel Comics",
	"biografia": "Bruce Banner, científico transformado en monstruo verde con fuerza increíble."
  },
  {
	"nombre": "Black Widow",
	"año_aparicion": 1964,
	"casa_comic": "Marvel Comics",
	"biografia": "Natasha Romanoff, espía rusa y experta en combate mano a mano y armas."
  },
  {
	"nombre": "Mr. Fantástico",
	"año_aparicion": 1961,
	"casa_comic": "Marvel Comics",
	"biografia": "Líder de los 4 Fantásticos, científico brillante con la capacidad de estirar y deformar su cuerpo."
  },
  {
	"nombre": "La Mujer Invisible",
	"año_aparicion": 1961,
	"casa_comic": "Marvel Comics",
	"biografia": "Miembro de los 4 Fantásticos, posee el poder de hacerse invisible y crear campos de fuerza."
  },
  {
	"nombre": "La Antorcha Humana",
	"año_aparicion": 1961,
	"casa_comic": "Marvel Comics",
	"biografia": "Miembro de los 4 Fantásticos, puede envolverse en llamas y volar a altas velocidades."
  },
  {
	"nombre": "La Cosa",
	"año_aparicion": 1961,
	"casa_comic": "Marvel Comics",
	"biografia": "Miembro de los 4 Fantásticos, posee una fuerza y resistencia sobrehumanas, con piel rocosa."
  },
  {
	"nombre": "Capitán América",
	"año_aparicion": 1941,
	"casa_comic": "Marvel Comics",
	"biografia": "El supersoldado Steve Rogers, símbolo de libertad y justicia con escudo indestructible."
  },
  {
	"nombre": "Ant-Man",
	"año_aparicion": 1962,
	"casa_comic": "Marvel Comics",
	"biografia": "Hanbiografiak Pym o Scott Lang, héroes capaces de cambiar de tamaño y comunicarse con insectos. Usa un traje que lo hace pequeño."
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


# A. Eliminar el nodo que contiene la información de Linterna Verde.
print("A:")
print("Índice de Linterna Verde (antes):", search(superheroes, "nombre", "Linterna Verde"))
remove(superheroes, "nombre", "Linterna Verde")
print("Índice de Linterna Verde (después):", search(superheroes, "nombre", "Linterna Verde"))


# B. Mostrar el año de aparición de Wolverine.
print("\nB:")
indice = search(superheroes, "nombre", "Wolverine")
print(f"Año de aparición de Wolverine: {superheroes[indice]["año_aparicion"]}.")


# C. Cambiar la casa de Dr. Strange a Marvel.
print("\nC:") #Doctor Strange ya pertenece a Marvel, pero asumo que el enunciado se refiere a cambiar de "Marvel Comics" a "Marvel".
indice = search(superheroes, "nombre", "Doctor Strange")
print(f"Casa de Doctor Strange (antes): {superheroes[indice]["casa_comic"]}.")
superheroes[indice]["casa_comic"] = "Marvel"
print(f"Casa de Doctor Strange (después): {superheroes[indice]["casa_comic"]}.")


# D. Mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra “traje” o “armadura”.
print("\nD:")
busqueda = []
for diccionario in superheroes:
	if "traje" in diccionario["biografia"] or "armadura" in diccionario["biografia"]:
		busqueda.append(diccionario["nombre"])
print(f"Superhéroes con 'traje' o 'armadura' en su biografía: {", ".join(busqueda)}.")


# E. Mostrar el nombre y la casa de los superhéroes cuya fecha de aparición sea anterior a 1963.
print("\nE:")
busqueda = []
for diccionario in superheroes:
	if diccionario["año_aparicion"] < 1963:
		busqueda.append({"nombre": diccionario["nombre"], "casa_comic": diccionario["casa_comic"]})
print("Nombres y casas de personajes que aparecieron antes de 1963:")
ordenar(busqueda, "nombre")
for elemento in busqueda:
	print(f"{elemento["nombre"]}: {elemento["casa_comic"]}.")


# F. Mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla.
print("\nF:")
indice = search(superheroes, "nombre", "Capitana Marvel")
print(f"Capitana Marvel pertenece a la casa {superheroes[indice]["casa_comic"]}.")
indice = search(superheroes, "nombre", "Mujer Maravilla")
print(f"Mujer Maravilla pertenece a la casa {superheroes[indice]["casa_comic"]}.")


# G. Mostrar toda la información de Flash y Star-Lord.
print("\nG:")
indice = search(superheroes, "nombre", "Flash")
info = list(superheroes[indice].items())
print("* Información sobre Flash:")
for elemento in info:
	print(f"{elemento[0]}: {elemento[1]}")
indice = search(superheroes, "nombre", "Star-Lord")
info = list(superheroes[indice].items())
print("* Información sobre Star-Lord:")
for elemento in info:
	print(f"{elemento[0]}: {elemento[1]}")


# H. Listar los superhéroes que comienzan con la letra B, M y S.
print("\nH:")
busqueda = []
for diccionario in superheroes:
	if diccionario["nombre"].startswith(("B", "M", "S")):
		busqueda.append(diccionario["nombre"])
print("Listado de superhéroes que comienzan con la letra B, M y S:")
busqueda.sort()
for elemento in busqueda:
	print(elemento)


# I. Determinar cuántos superhéroes hay de cada casa de comic.
print("\nI:")
Marvel = sum(1 for heroe in superheroes if heroe['casa_comic'] == 'Marvel Comics')
DC = sum(1 for heroe in superheroes if heroe['casa_comic'] == 'DC Comics')
print(f"Cantidad de superhérores de Marvel Comics: {Marvel}.")
print(f"Cantidad de superhérores de DC Comics: {DC}.")