class Stack:

    def __init__(self):
        self.__elements = []

    def push(self, element):
        self.__elements.append(element)

    def pop(self):
        if len(self.__elements) > 0:
            return self.__elements.pop()
        else:
            return None

    def on_top(self):
        if len(self.__elements) > 0:
            return self.__elements[-1]
        else:
            return None

    def size(self):
        return len(self.__elements)

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
    
    def tamaño(self):
        return len(self.__elementos)

