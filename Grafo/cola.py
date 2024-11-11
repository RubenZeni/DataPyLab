class Cola:
    def __init__(self):
        self.__elementos = []
    
    def arribo(self, elemento):
        self.__elementos.append(elemento)
    
    def atencion(self):
        if len(self.__elementos) > 0:
            return self.__elementos.pop(0)
        else:
            return None
    
    def tamanio(self):
        return len(self.__elementos)
    
    def en_frente(self):
        if len(self.__elementos) > 0:
            return self.__elementos[0]
        else:
            return None
    
    def mover_al_final(self):
        if len(self.__elementos) > 0:
            self.__elementos.append(self.__elementos.pop(0))