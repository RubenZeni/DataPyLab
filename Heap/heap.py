class HeapMax():

    def __init__(self):
        self.elementos = []
    
    def agregar(self, valor):
        self.elementos.append(valor)
        self.flotar(len(self.elementos)-1)

    def eliminar(self):
        if len(self.elementos) > 0:
            self.intercambiar(0, len(self.elementos)-1)
            valor = self.elementos.pop()
            self.hundir(0)
            return valor
        else:
            return None

    def intercambiar(self, indice_1, indice_2):
        self.elementos[indice_1], self.elementos[indice_2] = self.elementos[indice_2], self.elementos[indice_1]

    def flotar(self, indice):
        padre = (indice-1) // 2
        while indice > 0 and self.elementos[indice] > self.elementos[padre]:
            self.intercambiar(indice, padre)
            indice = padre
            padre = (indice-1) // 2

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
    
    def arribo(self, valor, prioridad):
        self.agregar([prioridad, valor])

    def atencion(self):
        return self.eliminar()

    def cambiar_prioridad(self, indice, nueva_prioridad):
        if indice < len(self.elementos):
            prioridad_anterior = self.elementos[indice][0]
            self.elementos[indice][0] = nueva_prioridad
            if nueva_prioridad > prioridad_anterior:
                self.flotar(indice)
            elif nueva_prioridad < prioridad_anterior:
                self.hundir(indice)


class HeapMin():

    def __init__(self):
        self.elementos = []
    
    def agregar(self, valor):
        self.elementos.append(valor)
        self.flotar(len(self.elementos)-1)

    def eliminar(self):
        if len(self.elementos) > 0:
            self.intercambiar(0, len(self.elementos)-1)
            valor = self.elementos.pop()
            self.hundir(0)
            return valor
        else:
            return None

    def intercambiar(self, indice_1, indice_2):
        self.elementos[indice_1], self.elementos[indice_2] = self.elementos[indice_2], self.elementos[indice_1]

    def flotar(self, indice):
        padre = (indice-1) // 2
        while indice > 0 and self.elementos[indice] < self.elementos[padre]:
            self.intercambiar(indice, padre)
            indice = padre
            padre = (indice-1) // 2

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
        for i in range(elementos_amontonados):
            valor = self.eliminar()
            resultado.append(valor)
        return resultado


    def arribo(self, valor, prioridad):
        self.agregar([prioridad, valor])

    def atencion(self):
        return self.eliminar()

    def cambiar_prioridad(self, indice, nueva_prioridad):
        if indice < len(self.elementos):
            prioridad_anterior = self.elementos[indice][0]
            self.elementos[indice][0] = nueva_prioridad
            if nueva_prioridad < prioridad_anterior:
                self.flotar(indice)
            elif nueva_prioridad > prioridad_anterior:
                self.hundir(indice)
    

    #A. Determinar el nombre del personaje de la superhéroe Capitana Marvel
    def encontrar_personaje_por_heroe(self, nombre_heroe):
        for elemento in self.elementos:
            if elemento[1]["heroe"] == nombre_heroe:
                return elemento[1]["nombre"]
        return None

    #B. Mostrar los nombres de los superhéroes femeninos
    def mostrar_superheroes_femeninos(self):
        for elemento in self.elementos:
            if elemento[1]["genero"] == "F":
                print(f'{elemento[1]["heroe"]} es femenina')

    #C. Mostrar los nombres de los personajes masculinos
    def mostrar_personajes_masculinos(self):
        for elemento in self.elementos:
            if elemento[1]["genero"] == "M":
                print(f'{elemento[1]["nombre"]} es masculino')

    #D. Determinar el nombre del superhéroe del personaje Scott Lang
    def encontrar_heroe_por_personaje(self, nombre_personaje):
        for elemento in self.elementos:
            if elemento[1]["nombre"] == nombre_personaje:
                return elemento[1]["heroe"]
        return None

    # E. Mostrar todos los datos de los superhéroes o personajes cuyos nombres comienzan con 'S'
    def mostrar_personajes_por_inicial(self, inicial):
        for elemento in self.elementos:
            if elemento[1]["nombre"].startswith(inicial):
                print(f"Personaje: {elemento[1]["nombre"]}\nNombre de superhéroe: {elemento[1]["heroe"]}\nGénero: {"Masculino" if elemento[1]["genero"]=="M" else "Femenino" if elemento[1]["genero"]=="F" else "Desconocido"}.")
            elif elemento[1]["heroe"].startswith(inicial):
                print(f"Héroe: {elemento[1]["heroe"]}\nNombre de personaje: {elemento[1]["nombre"]}\nGénero: {"Masculino" if elemento[1]["genero"]=="M" else "Femenino" if elemento[1]["genero"]=="F" else "Desconocido"}.")

    # F. Determinar si Carol Danvers está en el heap e indicar su superhéroe
    def encontrar_carol_danvers(self):
        for elemento in self.elementos:
            if elemento[1]["nombre"] == "Carol Danvers":
                return elemento[1]["heroe"]
        return None