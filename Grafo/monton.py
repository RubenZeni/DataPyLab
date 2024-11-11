class MontonMax():
	def __init__(self):
		self.elementos = []
	
	def agregar(self, valor):
		self.elementos.append(valor)
		self.flotar(len(self.elementos) - 1)
	
	def eliminar(self):
		if len(self.elementos) > 0:
			self.intercambiar(0, len(self.elementos) - 1)
			valor = self.elementos.pop()
			self.hundir(0)
			return valor
		else:
			return None
	
	def intercambiar(self, indice_1, indice_2):
		self.elementos[indice_1], self.elementos[indice_2] = self.elementos[indice_2], self.elementos[indice_1]
	
	def flotar(self, indice):
		padre = (indice - 1) // 2
		while indice > 0 and self.elementos[indice] > self.elementos[padre]:
			self.intercambiar(indice, padre)
			indice = padre
			padre = (indice - 1) // 2
	
	def hundir(self, indice):
		hijo_izquierdo = (indice * 2) + 1
		control = True
		while control and hijo_izquierdo < len(self.elementos):
			hijo_derecho = (indice * 2) + 2
			max = hijo_izquierdo
			if hijo_derecho < len(self.elementos):
				if self.elementos[hijo_derecho] > self.elementos[hijo_izquierdo]:
					max = hijo_derecho
			if self.elementos[indice] < self.elementos[max]:
				self.intercambiar(indice, max)
				indice = max
				hijo_izquierdo = (indice * 2) + 1
			else:
				control = False
	
	def amontonar(self, elementos):
		self.elementos = elementos
		for i in range(len(self.elementos)):
			self.flotar(i)
	
	def ordenar(self):
		resultado = []
		elementos_amontonados = len(self.elementos)
		for _ in range(elementos_amontonados):
			valor = self.eliminar()
			resultado.append(valor)
		return resultado
	
	def buscar(self, valor):
		for indice, elemento in enumerate(self.elementos):
			if elemento[1][0] == valor:
				return indice
	
	def arribo(self, valor, prioridad):
		self.agregar([prioridad, valor])
	
	def atencion(self):
		return self.eliminar()
	
	def cambiar_prioridad(self, indice, nueva_prioridad):
		if indice < len(self.elementos):
			anterior_prioridad = self.elementos[indice][0]
			self.elementos[indice][0] = nueva_prioridad
			if nueva_prioridad > anterior_prioridad:
				self.flotar(indice)
			elif nueva_prioridad < anterior_prioridad:
				self.hundir(indice)


class MontonMin():
	def __init__(self):
		self.elementos = []
	
	def agregar(self, valor):
		self.elementos.append(valor)
		self.flotar(len(self.elementos) - 1)
	
	def eliminar(self):
		if len(self.elementos) > 0:
			self.intercambiar(0, len(self.elementos) - 1)
			valor = self.elementos.pop()
			self.hundir(0)
			return valor
		else:
			return None
	
	def intercambiar(self, indice_1, indice_2):
		self.elementos[indice_1], self.elementos[indice_2] = self.elementos[indice_2], self.elementos[indice_1]
	
	def flotar(self, indice):
		padre = (indice - 1) // 2
		while indice > 0 and self.elementos[indice] < self.elementos[padre]:
			self.intercambiar(indice, padre)
			indice = padre
			padre = (indice - 1) // 2
	
	def hundir(self, indice):
		hijo_izquierdo = (indice * 2) + 1
		control = True
		while control and hijo_izquierdo < len(self.elementos):
			hijo_derecho = (indice * 2) + 2
			min = hijo_izquierdo
			if hijo_derecho < len(self.elementos):
				if self.elementos[hijo_derecho] < self.elementos[hijo_izquierdo]:
					min = hijo_derecho
			if self.elementos[indice] > self.elementos[min]:
				self.intercambiar(indice, min)
				indice = min
				hijo_izquierdo = (indice * 2) + 1
			else:
				control = False
	
	def amontonar(self, elementos):
		self.elementos = elementos
		for i in range(len(self.elementos)):
			self.flotar(i)
	
	def ordenar(self):
		resultado = []
		elementos_amontonados = len(self.elementos)
		for _ in range(elementos_amontonados):
			valor = self.eliminar()
			resultado.append(valor)
		return resultado
	
	def buscar(self, valor):
		for indice, elemento in enumerate(self.elementos):
			if elemento[1][0] == valor:
				return indice
	
	def arribo(self, valor, prioridad):
		self.agregar([prioridad, valor])
	
	def atencion(self):
		return self.eliminar()
	
	def cambiar_prioridad(self, indice, nueva_prioridad):
		if indice < len(self.elementos):
			anterior_prioridad = self.elementos[indice][0]
			self.elementos[indice][0] = nueva_prioridad
			if nueva_prioridad < anterior_prioridad:
				self.flotar(indice)
			elif nueva_prioridad > anterior_prioridad:
				self.hundir(indice)


# h = MontonMin()
# h.agregar(17)
# h.agregar(3)
# h.agregar(20)
# h.agregar(1)
# h.agregar(15)
# h.agregar(30)
# print(h.elementos)
# a = input()
# elementos = [19, 50, 10, 0, 40, 25]
# h.amontonar(elementos)
# print(h.elementos)
# a =input()
# print(h.ordenar())

# nombres = ['Ana', 'Kuan', 'Mario', 'Julieta', 'Pepito', 'Lola']
# from random import randint

# for nombre in nombres:
#     prioridad = randint(1,3)
#     h.arribo(nombre, prioridad)

#     print(h.elementos)
#     a = input()

# while len(h.elementos) > 0:
#     print(h.atencion())

# h.elementos = [[1, 'PEpito'], [1, 'Mario'], [1, 'Ana'], [2, 'Juan'], [2, 'Julieta'], [3, 'Lola']]

# h.cambiar_prioridad(0, 3)

# print(h.elementos)
# a = input()
# while len(h.elementos) > 0:
#     print(h.atencion())