class TablaHash:
	def __init__(self, size=10):
		self.size = size
		self.tabla = [[] for _ in range(self.size)]

	def funcion_hash(self, clave):
		return hash(clave) % self.size

	def insertar(self, clave, valor):
		indice = self.funcion_hash(clave)
		for item in self.tabla[indice]:
			if item[0] == clave:
				item[1] = valor
				return
		self.tabla[indice].append([clave, valor])

	def buscar(self, clave):
		indice = self.funcion_hash(clave)
		for item in self.tabla[indice]:
			if item[0] == clave:
				return item[1]
		return None

	def eliminar(self, clave):
		indice = self.funcion_hash(clave)
		for item in self.tabla[indice]:
			if item[0] == clave:
				self.tabla[indice].remove(item)
				return True
		return False


tabla = TablaHash(size = 5)

tabla.insertar("nombre", "Alice")
tabla.insertar("edad", 30)
tabla.insertar("ciudad", "New York")

print(tabla.buscar("edad"))

tabla.eliminar("ciudad")

print(tabla.buscar("ciudad"))
