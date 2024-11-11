class Pila:
    def __init__(self):
        self.__elementos = []
    
    def apilar(self, elemento):
        self.__elementos.append(elemento)
    
    def desapilar(self):
        if len(self.__elementos) > 0:
            return self.__elementos.pop()
        else:
            return None
    
    def cima(self):
        if len(self.__elementos) > 0:
            return self.__elementos[-1]
        else:
            return None
    
    def tamanio(self):
        return len(self.__elementos)

