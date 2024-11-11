from cola import Cola
from monton import MontonMin
from pila import Pila

class Grafo:
	def __init__(self, dirigido=True):
		self.elementos = []
		self.dirigido = dirigido

	def mostrar_grafo(self):
		print()
		print("nodos")
		for indice_1, nodo in enumerate(self.elementos):
			print(nodo["valor"])
			print(f"    aristas")
			for indice_2, elemento in enumerate(nodo["aristas"]):
				print(f"    destino {elemento["valor"]} peso: {elemento["peso"]}")
		print()

	def buscar(self, valor):
		for indice, elemento in enumerate(self.elementos):
			if elemento["valor"] == valor:
				return indice

	def buscar_arista(self, valor_vertice, valor):
		pos_origen = self.buscar(valor_vertice)
		if pos_origen is not None:
			for indice, elemento in enumerate(self.elementos[pos_origen]["aristas"]):
				if elemento["valor"] == valor:
					return pos_origen, indice

	def insertar_vertice(self, valor, otro_valor=None):
		nodo = {
		"valor": valor,
		"aristas": [],
		"visitado": False,
		}
		self.elementos.append(nodo)

	def insertar_arista(self, origen, destino, peso):
		pos_origen = self.buscar(origen)
		pos_destino = self.buscar(destino)
		if pos_origen is not None and pos_destino is not None:
			# print(origen, destino)
			arista = {
				"valor": destino,
				"peso": peso
			}
			self.elementos[pos_origen]["aristas"].append(arista)
			if not self.dirigido:
				arista = {
					"valor": origen,
					"peso": peso
				}
				self.elementos[pos_destino]["aristas"].append(arista)

	
	def eliminar_arista(self, origen, destino):
		resultado = self.buscar_arista(origen, destino)
		if resultado:
			pos_vertice, pos_arista = resultado
			valor = self.elementos[pos_vertice]["aristas"].pop(pos_arista)
			if not self.dirigido:
				resultado = self.buscar_arista(destino, origen)
				if resultado:
					pos_vertice, pos_arista = resultado
					self.elementos[pos_vertice]["aristas"].pop(pos_arista)
			return valor
	
	def eliminar_vertice(self, valor):
		pos_vertice = self.buscar(valor)
		if pos_vertice is not None:
			eliminar_valor = self.elementos.pop(pos_vertice)
			for nodo in self.elementos:
				self.eliminar_arista(nodo["valor"], valor)
			return eliminar_valor
	
	def marcar_no_visitado(self):
		for nodo in self.elementos:
			nodo["visitado"] = False

	def busqueda_de_profundidad(self, origen):
		def __busqueda_de_profundidad(grafo, origen):
			pos_vertice = grafo.buscar(origen)
			if pos_vertice is not None:
				if not grafo.elementos[pos_vertice]["visitado"]:
					grafo.elementos[pos_vertice]["visitado"] = True
					print(grafo.elementos[pos_vertice]["valor"])
					adyacentes = grafo.elementos[pos_vertice]["aristas"]
					for adyacente in adyacentes:
						__busqueda_de_profundidad(grafo, adyacente["valor"])
		
		self.marcar_no_visitado()
		__busqueda_de_profundidad(self, origen)

	def busqueda_de_amplitud(self, origen):
		self.marcar_no_visitado()
		cola = Cola()
		pos_vertice = self.buscar(origen)
		if pos_vertice is not None:
			if not self.elementos[pos_vertice]["visitado"]:
				cola.arribo(self.elementos[pos_vertice])
				while cola.tamanio() > 0:
					nodo = cola.atencion()
					nodo["visitado"] = True
					print(nodo["valor"])
					adyacentes = nodo["aristas"]
					for adyacente in adyacentes:
						pos_adyacente = self.buscar(adyacente["valor"])
						if not self.elementos[pos_adyacente]["visitado"]:
							cola.arribo(self.elementos[pos_adyacente])
	
	def existe_camino(self, origen, destino):
		def __existe_camino(grafo, origen, destino):
			resultado = False
			pos_vertice = grafo.buscar(origen)
			if pos_vertice is not None:
				if not grafo.elementos[pos_vertice]["visitado"]:
					grafo.elementos[pos_vertice]["visitado"] = True
					if grafo.elementos[pos_vertice]["valor"] == destino:
						return True
					else:
						adyacentes = grafo.elementos[pos_vertice]["aristas"]
						for adyacente in adyacentes:
							resultado = __existe_camino(grafo, adyacente["valor"], destino)
							if resultado:
								break
			return resultado
		
		self.marcar_no_visitado()
		resultado = __existe_camino(self, origen, destino)
		return resultado

	def dijkstra(self, origen):
		from math import inf
		no_visitados = MontonMin()
		camino = Pila()
		for nodo_1 in self.elementos:
			distancia = 0 if nodo_1["valor"] == origen else inf
			no_visitados.arribo([nodo_1["valor"], nodo_1, None], distancia)
		while len(no_visitados.elementos) > 0:
			nodo_2 = no_visitados.atencion()
			costo_nodo_actual = nodo_2[0]
			camino.apilar(nodo_2)
			adyacentes = nodo_2[1][1]["aristas"]
			# print(costo_nodo_actual, adjacentes)
			for adyacente in adyacentes:
				pos = no_visitados.buscar(adyacente["valor"])
				if pos is not None:
					if costo_nodo_actual + adyacente["peso"] < no_visitados.elementos[pos][0]:
						no_visitados.elementos[pos][1][2] = nodo_2[1][0]
						no_visitados.cambiar_prioridad(pos, costo_nodo_actual + adyacente["peso"])
		return camino

	def kruskal(self, origen):
		def buscar_en_bosque(bosque, buscado):
			for indice, arbol in enumerate(bosque):
				# print(buscado, arbol)
				if buscado in arbol:
					return indice

		bosque = []
		aristas = MontonMin()
		for nodo in self.elementos:
			bosque.append(nodo["valor"])
			adyacentes = nodo["aristas"]
			for adyacente in adyacentes:
				aristas.arribo([nodo["valor"], adyacente["valor"]], adyacente["peso"])

		# print(aristas.elementos)
		while len(bosque) > 1 and len(aristas.elementos) > 0:
			arista = aristas.atencion()
			# print(bosque)
			# print(arista[1][0], arista[1][1])
			# print(arista)
			origen = buscar_en_bosque(bosque, arista[1][0])
			destino = buscar_en_bosque(bosque, arista[1][1])
			# print(origen, destino)
			if origen is not None and destino is not None:
				if origen != destino:
					if origen > destino:
						vertice_ori = bosque.pop(origen)
						vertice_des = bosque.pop(destino)
					else:
						vertice_des = bosque.pop(destino)
						vertice_ori = bosque.pop(origen)

					if "-" not in vertice_ori and "-" not in vertice_des:
						bosque.append(f"{vertice_ori}-{vertice_des}-{arista[0]}")
					elif "-" not in vertice_des:
						bosque.append(vertice_ori+";"+f"{arista[1][0]}-{vertice_des}-{arista[0]}")
					elif "-" not in vertice_ori:
						bosque.append(vertice_des+";"+f"{vertice_ori}-{arista[1][1]}-{arista[0]}")
					else:
						bosque.append(vertice_ori+";"+vertice_des+";"+f"{arista[1][0]}-{arista[1][1]}-{arista[0]}")
		return bosque