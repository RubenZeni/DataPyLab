# Dada una cola con personajes de la saga Star Wars, de los cuales se conoce su nombre y planeta de origen. Desarrollar las funciones necesarias para resolver las siguientes actividades:
from cola import Cola

personajes_star_wars = [
	{"nombre": "Luke Skywalker", "planeta_natal": "Tatooine"},
	{"nombre": "Leia Organa", "planeta_natal": "Alderaan"},
	{"nombre": "Han Solo", "planeta_natal": "Corellia"},
	{"nombre": "Darth Vader", "planeta_natal": "Tatooine"},
	{"nombre": "Obi-Wan Kenobi", "planeta_natal": "Stewjon"},
	{"nombre": "Yoda", "planeta_natal": "Desconocido"},
	{"nombre": "Palpatine", "planeta_natal": "Naboo"},
	{"nombre": "Chewbacca", "planeta_natal": "Kashyyyk"},
	{"nombre": "Rey", "planeta_natal": "Jakku"},
	{"nombre": "Finn", "planeta_natal": "Desconocido"},
	{"nombre": "Wicket W. Warrick", "planeta_natal": "Endor"},
	{"nombre": "Kylo Ren", "planeta_natal": "Chandrila"},
	{"nombre": "Qui-Gon Jinn", "planeta_natal": "Coruscant"},
	{"nombre": "Padmé Amidala", "planeta_natal": "Naboo"},
	{"nombre": "Mace Windu", "planeta_natal": "Haruun Kal"}
]

cola_star_wars = Cola()
for personaje in personajes_star_wars:
	cola_star_wars.arribo(personaje)


# A. Mostrar los personajes del planeta Alderaan, Endor y Tatooine.
print("A:")
cola_encontrados = Cola()
for _ in range(cola_star_wars.tamaño()):
	if cola_star_wars.en_frente()["planeta_natal"] in ["Alderaan", "Endor", "Tatooine"]:
		cola_encontrados.arribo(cola_star_wars.en_frente())
	cola_star_wars.mover_al_final()
for _ in range(cola_encontrados.tamaño()):
	print(f"{cola_encontrados.en_frente()["nombre"]} es del planeta {cola_encontrados.atencion()["planeta_natal"]}")


# B. Indicar el plantea natal de Luke Skywalker y Han Solo.
print("\nB:")
cola_planetas = Cola()
for _ in range(cola_star_wars.tamaño()):
	if cola_star_wars.en_frente()["nombre"] in ["Luke Skywalker", "Han Solo"]:
		cola_planetas.arribo(cola_star_wars.en_frente())
	cola_star_wars.mover_al_final()
print(f"{cola_planetas.en_frente()["nombre"]} es del planeta {cola_planetas.atencion()["planeta_natal"]}, y ", end = "")
print(f"{cola_planetas.en_frente()["nombre"]} es del planeta {cola_planetas.atencion()["planeta_natal"]}.")


# C. Insertar un nuevo personaje antes del maestro Yoda.
print("\nC:")
personaje_nuevo = {"nombre": "Jar Jar Binks", "planeta_natal": "Naboo"}
for _ in range(cola_star_wars.tamaño()):
	if cola_star_wars.en_frente()["nombre"] == "Yoda":
		cola_star_wars.arribo(personaje_nuevo)
	cola_star_wars.mover_al_final()
print(f"Se agregó al personaje {personaje_nuevo["nombre"]} del planeta {personaje_nuevo["planeta_natal"]} antes del maestro Yoda.\n")
print("Barrido de la cola de personajes:")
for _ in range(cola_star_wars.tamaño()): # Mostrar cola para verificar la inserción del personaje.
	print(cola_star_wars.en_frente()["nombre"])
	cola_star_wars.mover_al_final()


# D. Eliminar el personaje ubicado después de Jar Jar Binks.
print("\nD:")
for indice in range(cola_star_wars.tamaño()):
	if cola_star_wars.en_frente()["nombre"] == "Jar Jar Binks":
		binks = 1 if indice < cola_star_wars.tamaño() else 2
	else:
		binks = 0
	cola_star_wars.mover_al_final()
	if binks == 1:
		eliminado = cola_star_wars.atencion()
print(f"Se eliminó al personaje {eliminado["nombre"]} del planeta {eliminado["planeta_natal"]} ubicado después de Jar Jar Binks.\n")
print("Barrido de la cola de personajes:")
for _ in range(cola_star_wars.tamaño()): # Mostrar cola para verificar la eliminación del personaje.
	print(cola_star_wars.en_frente()["nombre"])
	cola_star_wars.mover_al_final()