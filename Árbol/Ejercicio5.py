from arbol_avl import ArbolBinario
from cola import Cola

personajes_mcu = [
  {
	"nombre": "Wolverine",
	"año_aparicion": 1974,
	"casa_comic": "Marvel Comics",
	"biografia": "Mutante con garras retráctiles y habilidades regenerativas, miembro de los X-Men.",
	"villano": False
  },
  {
	"nombre": "Dortor Strange",
	"año_aparicion": 1963,
	"casa_comic": "Marvel Comics",
	"biografia": "Hechicero supremo del universo Marvel, maestro de las artes místicas y protector de la realidad.",
	"villano": False
  },
  {
	"nombre": "Capitana Marvel",
	"año_aparicion": 1968,
	"casa_comic": "Marvel Comics",
	"biografia": "Heroína cósmica con poderes de vuelo, fuerza sobrehumana y energía cósmica.",
	"villano": False
  },
  {
	"nombre": "Star-Lord",
	"año_aparicion": 1976,
	"casa_comic": "Marvel Comics",
	"biografia": "Líder de los Guardianes de la Galaxia, experto en combate y estrategia intergaláctica.",
	"villano": False
  },
  {
	"nombre": "Iron Man",
	"año_aparicion": 1963,
	"casa_comic": "Marvel Comics",
	"biografia": "Tony Stark, genio multimillonario y superhéroe con una armadura tecnológica de alta tecnología.",
	"villano": False
  },
  {
	"nombre": "Spider-Man",
	"año_aparicion": 1962,
	"casa_comic": "Marvel Comics",
	"biografia": "Peter Parker, joven héroe con habilidades arácnidas tras ser picado por una araña radiactiva.",
	"villano": False
  },
  {
	"nombre": "Thor",
	"año_aparicion": 1962,
	"casa_comic": "Marvel Comics",
	"biografia": "Dios nórdico del trueno y miembro de los Vengadores, posee un martillo encantado llamado Mjolnir.",
	"villano": False
  },
  {
	"nombre": "Hulk",
	"año_aparicion": 1962,
	"casa_comic": "Marvel Comics",
	"biografia": "Bruce Banner, científico transformado en monstruo verde con fuerza increíble.",
	"villano": False
  },
  {
	"nombre": "Black Widow",
	"año_aparicion": 1964,
	"casa_comic": "Marvel Comics",
	"biografia": "Natasha Romanoff, espía rusa y experta en combate mano a mano y armas.",
	"villano": False
  },
  {
	"nombre": "Mr. Fantástico",
	"año_aparicion": 1961,
	"casa_comic": "Marvel Comics",
	"biografia": "Líder de los 4 Fantásticos, científico brillante con la capacidad de estirar y deformar su cuerpo.",
	"villano": False
  },
  {
	"nombre": "La Mujer Invisible",
	"año_aparicion": 1961,
	"casa_comic": "Marvel Comics",
	"biografia": "Miembro de los 4 Fantásticos, posee el poder de hacerse invisible y crear campos de fuerza.",
	"villano": False
  },
  {
	"nombre": "La Antorcha Humana",
	"año_aparicion": 1961,
	"casa_comic": "Marvel Comics",
	"biografia": "Miembro de los 4 Fantásticos, puede envolverse en llamas y volar a altas velocidades.",
	"villano": False
  },
  {
	"nombre": "La Cosa",
	"año_aparicion": 1961,
	"casa_comic": "Marvel Comics",
	"biografia": "Miembro de los 4 Fantásticos, posee una fuerza y resistencia sobrehumanas, con piel rocosa.",
	"villano": False
  },
  {
	"nombre": "Capitán América",
	"año_aparicion": 1941,
	"casa_comic": "Marvel Comics",
	"biografia": "El supersoldado Steve Rogers, símbolo de libertad y justicia con escudo indestructible.",
	"villano": False
  },
  {
	"nombre": "Thanos",
	"año_aparicion": 1973,
	"casa_comic": "Marvel Comics",
	"biografia": "Uno de los villanos más poderosos del MCU, busca reunir las Gemas del Infinito para controlar el universo.",
	"villano": True
  },
  {
	"nombre": "Loki",
	"año_aparicion": 1962,
	"casa_comic": "Marvel Comics",
	"biografia": "Dios de las mentiras y la travesura, hermano adoptivo de Thor, suele alternar entre ser villano y antihéroe.",
	"villano": True
  },
  {
	"nombre": "Ultron",
	"año_aparicion": 1968,
	"casa_comic": "Marvel Comics",
	"biografia": "Inteligencia artificial creada por Tony Stark, se rebela contra la humanidad y busca exterminarla.",
	"villano": True
  },
  {
	"nombre": "Hela",
	"año_aparicion": 1964,
	"casa_comic": "Marvel Comics",
	"biografia": "Diosa de la muerte y hermana de Thor, busca dominar Asgard y destruir a los Vengadores.",
	"villano": True
  },
  {
	"nombre": "Cráneo Rojo",
	"año_aparicion": 1941,
	"casa_comic": "Marvel Comics",
	"biografia": "Antiguo líder de Hydra, enemigo acérrimo del Capitán América, obsesionado con el poder y el control del mundo.",
	"villano": True
  },
  {
	"nombre": "Venom",
	"año_aparicion": 1984,
	"casa_comic": "Marvel Comics",
	"biografia": "Simbionte alienígena que se une a Eddie Brock, transformándose en uno de los más temidos enemigos de Spider-Man.",
	"villano": True
  },
  {
	"nombre": "Mandarín",
	"año_aparicion": 1964,
	"casa_comic": "Marvel Comics",
	"biografia": "Villano con diez anillos que le otorgan poderes sobrehumanos, enemigo recurrente de Iron Man.",
	"villano": True
  },
  {
	"nombre": "Dormammu",
	"año_aparicion": 1964,
	"casa_comic": "Marvel Comics",
	"biografia": "Entidad poderosa de la Dimensión Oscura, enemigo de Doctor Strange y maestro de la magia oscura.",
	"villano": True
  }
]

# Dado un árbol con los nombres de los superhéroes y villanos de la saga Marvel Cinematic Universe (MCU), desarrollar un algoritmo que contemple lo siguiente:

# A. Además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo booleano que indica si es un héroe o un villano, True y False respectivamente.
print("A:")
arbol_personajes = ArbolBinario()
for personaje in personajes_mcu:
	arbol_personajes.insertar_nodo(personaje["nombre"], {"es_heroe": False if personaje["villano"] else True})
if arbol_personajes.raiz.otro_valor is not None:
	print("OK")
else:
	print("FAIL")


# B. Listar los villanos ordenados alfabéticamente.
print("\nB:\nLista de villanos ordenados alfabéticamente:")
arbol_personajes.inorden_villanos()


# C. Mostrar todos los superhéroes que empiezan con C.
print("\nC:\nSuperhérores que empiezan con C:")
arbol_personajes.busqueda_de_proximidad_superheroes("C")


# D. Determinar cuántos superhéroes hay el árbol.
print("\nD:")
conteo = arbol_personajes.contar_superheroes()
print("Hay un total de", conteo, "superhéroes en el árbol.")


# E. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para encontrarlo en el árbol y modificar su nombre.
print("\nE:\nBúsqueda de proximidad:")
arbol_personajes.busqueda_de_proximidad_modificacion("D") # Primer llamado a la función, para encontrar al personaje
print("Modificación del nombre...")
arbol_personajes.busqueda_de_proximidad_modificacion("D", 0, "Doctor Strange") # Segundo llamado a la función, para modificar el nombre del personaje
print("Verificación:")
arbol_personajes.busqueda_de_proximidad_modificacion("D") # Tercer llamado a la función, para verifiar la modificación previa


# F. Listar los superhéroes ordenados de manera descendente.
print("\nF:")
arbol_personajes.inorden_superheroes(reverse=True)

# G. Generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a los villanos, luego resolver las siguiente tareas:
def inorden_bosque(raiz=None, otro_arbol=None, heroe=True): # Función para la generación del bosque a partir del arbol existente. Recibe una raiz para el recorrido inorden, un árbol donde insertar los nuevos nodos y un bool para saber si separar heroes o villanos.
	otro_arbol = ArbolBinario() if not isinstance(otro_arbol, ArbolBinario) else otro_arbol # Si no recibe ArbolBinario otro_arbol, se instancia.
	if raiz is not None:
		otro_arbol = inorden_bosque(raiz=raiz.izquierda, otro_arbol=otro_arbol, heroe=heroe) # Recursividad con el hijo izquierdo
		# Inserta el nodo correspondiente según el bool heroe:
		if heroe and raiz.otro_valor.get("es_heroe"):
			otro_arbol.insertar_nodo(raiz.valor, raiz.otro_valor)
		elif not heroe and not raiz.otro_valor.get("es_heroe"):
			otro_arbol.insertar_nodo(raiz.valor, raiz.otro_valor)
		otro_arbol = inorden_bosque(raiz=raiz.derecha, otro_arbol=otro_arbol, heroe=heroe) # Recusrividad con el hijo derecho
	return otro_arbol # Retorno el nuevo árbol

arbol_villanos = inorden_bosque(raiz=arbol_personajes.raiz, heroe=False)
arbol_superheroes = inorden_bosque(raiz=arbol_personajes.raiz, heroe=True)

# 1. Determinar cuántos nodos tiene cada árbol.
print(f"\nG.I:\nEl árbol con superhéroes tiene un total de {arbol_superheroes.contar_nodos()} nodos.")
print(f"El árbol con villanos tiene un total de {arbol_villanos.contar_nodos()} nodos.")

# 2. Realizar un barrido ordenado alfabéticamente de cada árbol.
print("\nG.II:\n\nBarrido del árbol con superhéroes:")
arbol_superheroes.inorden()
print("\nBarrido del árbol con villanos:")
arbol_villanos.inorden()