from cola import Cola

class ArbolBinario:

	class __Nodo:
		def __init__(self, valor, izquierda=None, derecha=None, otro_valor=None):
			self.valor = valor
			self.izquierda = izquierda
			self.derecha = derecha
			self.otro_valor = otro_valor
			self.peso = 0
	
	def __init__(self):
		self.raiz = None
	
	def peso(self, raiz):
		if raiz is None:
			return -1
		else:
			return raiz.peso
	
	def actualizar_peso(self, raiz):
		if raiz is not None:
			raiz.peso = max(self.peso(raiz.izquierda), self.peso(raiz.derecha)) + 1
	
	def rotacion_simple(self, raiz, control):
		if control:
			aux = raiz.izquierda
			raiz.izquierda = aux.derecha
			aux.derecha = raiz
		else:
			aux = raiz.derecha
			raiz.derecha = aux.izquierda
			aux.izquierda = raiz
		self.actualizar_peso(raiz)
		self.actualizar_peso(aux)
		raiz = aux
		return raiz
	
	def rotacion_doble(self, raiz, control):
		if control:
			raiz.izquierda = self.rotacion_simple(raiz.izquierda, False)
			raiz = self.rotacion_simple(raiz, True)
		else:
			raiz.derecha = self.rotacion_simple(raiz.derecha, True)
			raiz = self.rotacion_simple(raiz, False)
		return raiz
	
	def balanceo(self, raiz):
		if raiz is not None:
			if self.peso(raiz.izquierda) - self.peso(raiz.derecha) == 2:
				if self.peso(raiz.izquierda.izquierda) >= self.peso(raiz.izquierda.derecha):
					raiz = self.rotacion_simple(raiz, True)
				else:
					raiz = self.rotacion_doble(raiz, True)
			elif self.peso(raiz.derecha) - self.peso(raiz.izquierda) == 2:
				if self.peso(raiz.derecha.derecha) >= self.peso(raiz.derecha.izquierda):
					raiz = self.rotacion_simple(raiz, False)
				else:
					raiz = self.rotacion_doble(raiz, False)
		return raiz
	
	def insertar_nodo(self, valor, otro_valor=None):
		def __insertar(raiz, valor, otro_valor=None):
			if raiz is None:
				return ArbolBinario.__Nodo(valor, otro_valor=otro_valor)
			elif valor < raiz.valor:
				raiz.izquierda = __insertar(raiz.izquierda, valor, otro_valor)
			else:
				raiz.derecha = __insertar(raiz.derecha, valor, otro_valor)
			raiz = self.balanceo(raiz)
			self.actualizar_peso(raiz)
			return raiz
		
		self.raiz = __insertar(self.raiz, valor, otro_valor)
	
	def busqueda(self, clave):
		def __buscar(raiz, clave):
			if raiz is not None:
				if raiz.valor == clave:
					return raiz
				elif clave < raiz.valor:
					return __buscar(raiz.izquierda, clave)
				else:
					return __buscar(raiz.derecha, clave)

		if self.raiz is not None:
			return __buscar(self.raiz, clave)
	
	def preorden(self):
		def __preorden(raiz):
			if raiz is not None:
				print(raiz.valor)
				__preorden(raiz.izquierda)
				__preorden(raiz.derecha)
		
		if self.raiz is not None:
			__preorden(self.raiz)
	
	def inorden(self):
		def __inorden(raiz):
			if raiz is not None:
				__inorden(raiz.izquierda)
				print(raiz.valor)
				__inorden(raiz.derecha)
		
		if self.raiz is not None:
			__inorden(self.raiz)
	
	def postorden(self):
		def __postorden(raiz):
			if raiz is not None:
				__postorden(raiz.derecha)
				print(raiz.valor)
				__postorden(raiz.izquierda)
		
		if self.raiz is not None:
			__postorden(self.raiz)
	
	def busqueda_de_proximidad(self, valor):
		def __buscar(raiz, valor):
			if raiz is not None:
				__buscar(raiz.izquierda, valor)
				if raiz.valor.startswith(valor):
					print(raiz.valor)
				__buscar(raiz.derecha, valor)
		
		if self.raiz is not None:
			__buscar(self.raiz, valor)
	
	def por_nivel(self):
		pendientes = Cola()
		if self.raiz is not None:
			pendientes.arribo(("--Raíz--", self.raiz, self.raiz.peso))
			nivel_aux = self.raiz.peso
		
		while pendientes.tamaño() > 0:
			direccion, raiz, nivel = pendientes.atencion()
			if nivel == nivel_aux:
				nivel_aux -= 1
				print(f"Nivel {nivel}:")
			print(f"   |{direccion}| {raiz.valor} (peso {raiz.peso}).")
			if raiz.izquierda is not None:
				pendientes.arribo((f"<--{raiz.valor}-- ", raiz.izquierda, nivel - 1))
			if raiz.derecha is not None:
				pendientes.arribo((f" --{raiz.valor}-->", raiz.derecha, nivel - 1))

	def eliminar_nodo(self, valor):
		def __reemplazar(raiz):
			if raiz.derecha is None:
				return raiz.izquierda, raiz
			else:
				raiz.derecha, nodo_reemplazado = __reemplazar(raiz.derecha)
				return raiz, nodo_reemplazado
		
		def __eliminar(raiz, valor):
			valor_borrado = None
			otro_valor_borrado = None
			if raiz is not None:
				if raiz.valor > valor:
					raiz.izquierda, valor_borrado, otro_valor_borrado = __eliminar(raiz.izquierda, valor)
				elif raiz.valor < valor:
					raiz.derecha, valor_borrado, otro_valor_borrado = __eliminar(raiz.derecha, valor)
				else:
					valor_borrado = raiz.valor
					otro_valor_borrado = raiz.otro_valor
					if raiz.izquierda is None:
						return raiz.derecha, valor_borrado, otro_valor_borrado
					elif raiz.derecha is None:
						return raiz.izquierda, valor_borrado, otro_valor_borrado
					else:
						raiz.izquierda, nodo_reemplazado = __reemplazar(raiz.izquierda)
						raiz.valor = nodo_reemplazado.valor
						raiz.otro_valor = nodo_reemplazado.otro_valor
					raiz = self.balanceo(raiz)
					self.actualizar_peso(raiz)
			return raiz, valor_borrado, otro_valor_borrado

		valor_borrado = None
		otro_valor_borrado = None
		if self.raiz is not None:
			self.raiz, valor_borrado, otro_valor_borrado = __eliminar(self.raiz, valor)
		return valor_borrado, otro_valor_borrado
	


	# Ejercicio 5:

	# B. Listar los villanos ordenados alfabéticamente.
	def inorden_villanos(self):
		def __inorden_villanos(raiz): # Función recursiva de barrido inorden, modificada con filtro "es_heroe"
			if raiz is not None:
				__inorden_villanos(raiz.izquierda)
				if not raiz.otro_valor.get("es_heroe"):
					print(raiz.valor)
				__inorden_villanos(raiz.derecha)
		if self.raiz is not None:
			__inorden_villanos(self.raiz) # Llamado a la función
	
	# C. Mostrar todos los superhéroes que empiezan con C.
	def busqueda_de_proximidad_superheroes(self, valor):
		def __busqueda_de_proximidad_superheroes(raiz, valor):
			if raiz is not None:
				__busqueda_de_proximidad_superheroes(raiz.izquierda, valor)
				if raiz.valor.startswith(valor) and raiz.otro_valor.get("es_heroe"):
					print(raiz.valor)
				__busqueda_de_proximidad_superheroes(raiz.derecha, valor)
		if self.raiz is not None:
			__busqueda_de_proximidad_superheroes(self.raiz, valor)
	
	# D. Determinar cuántos superhéroes hay el árbol.
	def contar_superheroes(self):
		def __contar_superheroes(raiz): # Función recursiva para contar los superheroes
			contador = 0
			if raiz is not None:
				if raiz.otro_valor.get("es_heroe"):
					contador = 1
				contador += __contar_superheroes(raiz.izquierda)
				contador += __contar_superheroes(raiz.derecha)
			return contador
		return 0 if self.raiz is None else __contar_superheroes(self.raiz)
	
	# E. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para encontrarlo en el árbol y modificar su nombre.
	def busqueda_de_proximidad_modificacion(self, valor, posicion=None, nuevo_valor=None):
		def __busqueda_de_proximidad_modificacion(raiz, valor, posicion=None, nuevo_valor=None, contador=0):
			if raiz is not None:
				if posicion is None:
					hit = True if raiz.valor.startswith(valor) else False
					__busqueda_de_proximidad_modificacion(raiz.izquierda, valor, posicion=posicion, nuevo_valor=nuevo_valor, contador=(contador + 1 if hit else contador))
					if hit:
						print(f"{contador} - {raiz.valor}")
					__busqueda_de_proximidad_modificacion(raiz.derecha, valor, posicion=posicion, nuevo_valor=nuevo_valor, contador=(contador + 1 if hit else contador))
				else:
					hit = True if raiz.valor.startswith(valor) else False
					__busqueda_de_proximidad_modificacion(raiz.izquierda, valor, posicion=posicion, nuevo_valor=nuevo_valor, contador=(contador + 1 if hit else contador))
					if hit:
						if posicion == contador and nuevo_valor is not None:
							raiz.valor = nuevo_valor
					__busqueda_de_proximidad_modificacion(raiz.derecha, valor, posicion=posicion, nuevo_valor=nuevo_valor, contador=(contador + 1 if hit else contador))
		if self.raiz is not None:
			__busqueda_de_proximidad_modificacion(self.raiz, valor, posicion=posicion, nuevo_valor=nuevo_valor, contador=0)
	
	# F. Listar los superhéroes ordenados de manera descendente.
	def inorden_superheroes(self, reverse=False):
		def __inorden_superheroes(raiz, reverse): # Función recursiva de barrido inorden, modificada con filtro "es_heroe"
			if raiz is not None:
				if not reverse:
					__inorden_superheroes(raiz.izquierda, reverse=reverse)
					if raiz.otro_valor.get("es_heroe"):
						print(raiz.valor)
					__inorden_superheroes(raiz.derecha, reverse=reverse)
				else:
					__inorden_superheroes(raiz.derecha, reverse=reverse)
					if raiz.otro_valor.get("es_heroe"):
						print(raiz.valor)
					__inorden_superheroes(raiz.izquierda, reverse=reverse)
		if self.raiz is not None:
			__inorden_superheroes(self.raiz, reverse=reverse) # Llamado a la función
	
	# G.I. Determinar cuántos nodos tiene cada árbol.
	def contar_nodos(self):
		def __contar_nodos(raiz): # Función recursiva para contar los nodos del arbol
			contador = 0
			if raiz is not None:
				contador = 1
				contador += __contar_nodos(raiz.izquierda)
				contador += __contar_nodos(raiz.derecha)
			return contador
		return 0 if self.raiz is None else __contar_nodos(self.raiz)



	# Ejercicio 23:

	# A. Listado inorden de las criaturas y quienes la derrotaron.
	def inorden_criaturas(self):
		def __inorden_criaturas(raiz): # Función recursiva de barrido inorden, modificada con filtro "es_heroe"
			if raiz is not None:
				__inorden_criaturas(raiz.izquierda)
				valor = "-" if raiz.valor is None else raiz.valor
				derrotada_por = "-" if raiz.otro_valor["derrotada_por"] is None else raiz.otro_valor["derrotada_por"]
				while True:
					if len(valor) < 23:
						valor += " "
					if len(derrotada_por) < 16:
						derrotada_por += " "
					if len(valor) == 23 and len(derrotada_por) == 16:
						break
				print(f"| {valor} | {derrotada_por} |")
				__inorden_criaturas(raiz.derecha)
		if self.raiz is not None:
			__inorden_criaturas(self.raiz) # Llamado a la función

	# B. Se debe permitir cargar una breve descripción sobre cada criatura.
	def insertar_descripcion(self, criatura, descripcion):
		def __insertar_descripcion(raiz, criatura, descripcion):
			if raiz is not None:
				if raiz.valor == criatura:
					raiz.otro_valor["descripcion"] = descripcion
					print(f"Criatura: {raiz.valor} - Descripcion: {raiz.otro_valor["descripcion"]}")
					return
				else:
					__insertar_descripcion(raiz.izquierda, criatura=criatura, descripcion=descripcion)
					__insertar_descripcion(raiz.derecha, criatura=criatura, descripcion=descripcion)
		if self.raiz is not None:
			__insertar_descripcion(self.raiz, criatura, descripcion)
	
	# C. Mostrar toda la información de la criatura Talos.
	def mostrar_informacion(self, criatura):
		raiz_criatura = self.busqueda(criatura)
		if raiz_criatura is not None:
			print(f"Criatura: {raiz_criatura.valor}")
			print(f"Derrotada por: {"Nadie" if raiz_criatura.otro_valor["derrotada_por"] is None else raiz_criatura.otro_valor["derrotada_por"]}")
			if "capturada" in raiz_criatura.otro_valor:
				print(f"Capturada por: {"Nadie" if raiz_criatura.otro_valor["capturada"] is None else raiz_criatura.otro_valor["capturada"]}")
			print(f"Descripción: {"Desconocida." if raiz_criatura.otro_valor["descripcion"] == "" else raiz_criatura.otro_valor["descripcion"]}")
	
	# D. Determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas.
	def top_3_heroes_dioses(self):
		def __top_3_heroes_dioses(raiz, heroes_dioses={}):
			if raiz is not None:
				if raiz.otro_valor["derrotada_por"] is not None:
					if raiz.otro_valor["derrotada_por"] not in heroes_dioses:
						heroes_dioses[raiz.otro_valor["derrotada_por"]] = 1
					else:
						heroes_dioses[raiz.otro_valor["derrotada_por"]] += 1
				__top_3_heroes_dioses(raiz.izquierda, heroes_dioses=heroes_dioses)
				__top_3_heroes_dioses(raiz.derecha, heroes_dioses=heroes_dioses)
			return heroes_dioses
		if self.raiz is not None:
			return __top_3_heroes_dioses(self.raiz)
	
	# E. Listar las criaturas derrotadas por Heracles.
	def cantidad_derrotadas_por(self, heroe_dios):
		def __cantidad_derrotadas_por(raiz, heroe_dios):
			cantidad = 0
			if raiz is not None:
				if raiz.otro_valor["derrotada_por"] == heroe_dios:
					cantidad = 1
				cantidad += __cantidad_derrotadas_por(raiz.izquierda, heroe_dios=heroe_dios)
				cantidad += __cantidad_derrotadas_por(raiz.derecha, heroe_dios=heroe_dios)
				return cantidad
			return 0
		if self.raiz is not None:
			return 0 if self.raiz is None else __cantidad_derrotadas_por(self.raiz, heroe_dios=heroe_dios)
	
	# F. Listar las criaturas que no han sido derrotadas.
	def criaturas_no_derrotadas(self):
		def __criaturas_no_derrotadas(raiz, criaturas=[]):
			if raiz is not None:
				if raiz.otro_valor["derrotada_por"] is None:
					criaturas.append(raiz.valor)
				__criaturas_no_derrotadas(raiz.izquierda, criaturas=criaturas)
				__criaturas_no_derrotadas(raiz.derecha, criaturas=criaturas)
			return criaturas
		if self.raiz is not None:
			return __criaturas_no_derrotadas(self.raiz)
	
	# G. Además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe o dios que la capturo.
	def agregar_modificar_campo(self, criatura, campo, valor):
		def __agregar_modificar_campo(raiz, criatura, campo, valor):
			if raiz is not None:
				if raiz.valor == criatura:
					raiz.otro_valor[campo] = valor
					print(f"Campo '{campo}' agregado o modificado con el valor {valor}.")
					return
				else:
					__agregar_modificar_campo(raiz.izquierda, criatura=criatura, campo=campo, valor=valor)
					__agregar_modificar_campo(raiz.derecha, criatura=criatura, campo=campo, valor=valor)
		if self.raiz is not None:
			__agregar_modificar_campo(self.raiz, criatura, campo, valor)
	
	# H. Modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de Erimanto indicando que Heracles las atrapó.
	def registrar_captura(self, criatura, heroe_dios):
		def __registrar_captura(raiz, criatura, heroe_dios):
			if raiz is not None:
				if raiz.valor == criatura:
					raiz.otro_valor["capturada"] = heroe_dios
					print(f"{criatura} capturada por {heroe_dios}.")
					return
				else:
					__registrar_captura(raiz.izquierda, criatura=criatura, heroe_dios=heroe_dios)
					__registrar_captura(raiz.derecha, criatura=criatura, heroe_dios=heroe_dios)
		if self.raiz is not None:
			__registrar_captura(self.raiz, criatura=criatura, heroe_dios=heroe_dios)
	
	# I. Se debe permitir búsquedas por coincidencia.
	def busqueda_por_coincidencia(self, valor):
		def __buscar_por_coincidencia(raiz, valor):
			nodos = []
			if raiz is not None:
				if valor in raiz.valor:
					nodos.append(raiz)
				nodos += __buscar_por_coincidencia(raiz.izquierda, valor)
				nodos += __buscar_por_coincidencia(raiz.derecha, valor)
			return nodos
		return [] if self.raiz is None else __buscar_por_coincidencia(self.raiz, valor)

	# K. Modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles derroto a varias.
	def registrar_derrota(self, criatura, heroe_dios):
		def __registrar_derrota(raiz, criatura, heroe_dios):
			if raiz is not None:
				if raiz.valor == criatura:
					raiz.otro_valor["derrotado_por"] = heroe_dios
					print(f"{criatura} derrotada por {heroe_dios}.")
					return
				else:
					__registrar_derrota(raiz.izquierda, criatura=criatura, heroe_dios=heroe_dios)
					__registrar_derrota(raiz.derecha, criatura=criatura, heroe_dios=heroe_dios)
		if self.raiz is not None:
			__registrar_derrota(self.raiz, criatura, heroe_dios=heroe_dios)

	# L. Modifique el nombre de la criatura Ladón por Dragón Ladón.
	def modificar_nombre_criatura(self, criatura, nombre):
		def __modificar_nombre_criatura(raiz, criatura, nombre):
			if raiz is not None:
				if raiz.valor == criatura:
					raiz.valor = nombre
					print(f"Se cambió el nombre de la criatura {criatura} a {nombre}.")
					return
				else:
					__modificar_nombre_criatura(raiz.izquierda, criatura=criatura, nombre=nombre)
					__modificar_nombre_criatura(raiz.derecha, criatura=criatura, nombre=nombre)
		if self.raiz is not None:
			__modificar_nombre_criatura(self.raiz, criatura=criatura, nombre=nombre)
			

	# N. Muestre las criaturas capturadas por Heracles.
	def criaturas_capturadas_por(self, heroe_dios):
		def __inorden(raiz, heroe_dios):
			criaturas = []
			if raiz is not None:
				if raiz.otro_valor["capturada"] == heroe_dios:
					criaturas.append(raiz.valor)
				criaturas += __inorden(raiz.izquierda, heroe_dios=heroe_dios)
				criaturas += __inorden(raiz.derecha, heroe_dios=heroe_dios)
			return criaturas
		if self.raiz is not None:
			return [] if self.raiz is None else __inorden(self.raiz, heroe_dios=heroe_dios)