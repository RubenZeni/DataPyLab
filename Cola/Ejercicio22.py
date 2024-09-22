# Se tienen una cola con personajes de Marvel Cinematic Universe (MCU), de los cuales se conoce el nombre del personaje, el nombre del superhéroe y su género (Masculino M y Femenino F) –por ejemplo {Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M}, {Natasha Romanoff, Black Widow, F}, etc., desarrollar un algoritmo que resuelva las siguientes actividades:
from cola import Cola

superheroes = [
	# Marvel
	{"nombre_real": "Carol Danvers", "nombre_superheroe": "Capitana Marvel", "genero": "F"},
	{"nombre_real": "Scott Lang", "nombre_superheroe": "Ant-Man", "genero": "M"},
	{"nombre_real": "Peter Parker", "nombre_superheroe": "Spider-Man", "genero": "M"},
	{"nombre_real": "Natasha Romanoff", "nombre_superheroe": "Black Widow", "genero": "F"},
	{"nombre_real": "Steve Rogers", "nombre_superheroe": "Captain America", "genero": "M"},
	{"nombre_real": "Wanda Maximoff", "nombre_superheroe": "Scarlet Witch", "genero": "F"},
	{"nombre_real": "Stephen Strange", "nombre_superheroe": "Doctor Strange", "genero": "M"},
	{"nombre_real": "Shuri", "nombre_superheroe": "Black Panther", "genero": "F"},
	{"nombre_real": "Jennifer Walters", "nombre_superheroe": "She-Hulk", "genero": "F"},
	# DC
	{"nombre_real": "Clark Kent", "nombre_superheroe": "Superman", "genero": "M"},
	{"nombre_real": "Bruce Wayne", "nombre_superheroe": "Batman", "genero": "M"},
	{"nombre_real": "Diana Prince", "nombre_superheroe": "Wonder Woman", "genero": "F"},
	{"nombre_real": "Selina Kyle", "nombre_superheroe": "Catwoman", "genero": "F"},
	{"nombre_real": "Barry Allen", "nombre_superheroe": "The Flash", "genero": "M"},
	{"nombre_real": "Kara Zor-El", "nombre_superheroe": "Supergirl", "genero": "F"},
	{"nombre_real": "Arthur Curry", "nombre_superheroe": "Aquaman", "genero": "M"}
]

cola_superheroes = Cola()
for personaje in superheroes:
	cola_superheroes.arribo(personaje)


# A. Determinar el nombre del personaje de la superhéroe Capitana Marvel.
print("A:")
for _ in range(cola_superheroes.tamaño()):
	if cola_superheroes.en_frente()["nombre_superheroe"] == "Capitana Marvel":
		nombre_real = cola_superheroes.en_frente()["nombre_real"]
	cola_superheroes.mover_al_final()
print(f"El nombre del personaje de la superhéroe Capitana Marvel es {nombre_real}.")


# B. Mostrar los nombres de los superhéroes femeninos.
print("\nB:")
cola_femeninos = Cola()
for _ in range(cola_superheroes.tamaño()):
	if cola_superheroes.en_frente()["genero"] == "F":
		cola_femeninos.arribo(cola_superheroes.en_frente())
	cola_superheroes.mover_al_final()
print("Nombres de los superhéroes femeninos:")
for _ in range(cola_femeninos.tamaño()):
	print(f"{cola_femeninos.atencion()["nombre_real"]}.")

# C. Mostrar los nombres de los personajes masculinos.
print("\nC:")
cola_masculinos = Cola()
for _ in range(cola_superheroes.tamaño()):
	if cola_superheroes.en_frente()["genero"] == "M":
		cola_masculinos.arribo(cola_superheroes.en_frente())
	cola_superheroes.mover_al_final()
print("Nombres de los superhéroes masculinos:")
for _ in range(cola_masculinos.tamaño()):
	print(f"{cola_masculinos.atencion()["nombre_real"]}.")


# D. Determinar el nombre de superhéroe del personaje Scott Lang.
print("\nD:")
for _ in range(cola_superheroes.tamaño()):
	if cola_superheroes.en_frente()["nombre_real"] == "Scott Lang":
		nombre_superheroe = cola_superheroes.en_frente()["nombre_superheroe"]
	cola_superheroes.mover_al_final()
print(f"El nombre de superhéroe del personaje Scott Lang es {nombre_superheroe}.")


# E. Mostrar todos los datos de los superhéroes o personajes cuyos nombres comienzan con la letra S.
print("\nE:")
cola_con_S = Cola()
for _ in range(cola_superheroes.tamaño()):
	if cola_superheroes.en_frente()["nombre_real"].startswith(("S")) or cola_superheroes.en_frente()["nombre_superheroe"].startswith(("S")):
		cola_con_S.arribo(cola_superheroes.en_frente())
	cola_superheroes.mover_al_final()
print("Nombres de los superhéroes o personajes cuyos nombres comienzan con la letra S:")
for _ in range(cola_con_S.tamaño()):
	print(f"Personaje: {cola_con_S.atencion()["nombre_real"]}." if cola_con_S.en_frente()["nombre_real"].startswith(("S")) else f"Superhéroe: {cola_con_S.atencion()["nombre_superheroe"]}.")

# F. Determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre de superhéroes.
print("\nD:")
nombre_superheroe = None
for _ in range(cola_superheroes.tamaño()):
	if cola_superheroes.en_frente()["nombre_real"] == "Carol Danvers":
		nombre_superheroe = cola_superheroes.en_frente()["nombre_superheroe"]
	cola_superheroes.mover_al_final()
if nombre_superheroe is not None:
	print(f"Carol Danvers se encuentra en la cola, y su nombre de superhéroe es {nombre_superheroe}.")
else:
	print("Carol Danvers no se encuentra en la cola.")