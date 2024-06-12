from pila import Stack
from dino import dinosaurios

pila_dinosaurios = Stack()
for dino in dinosaurios:
    pila_dinosaurios.push(dino)

def contar_especies(pila):
    especies = {}
    temp = []
    while pila.size() > 0:
        dino = pila.pop()
        temp.append(dino)
        if dino['especie'] not in especies:
            especies[dino['especie']] = True
    for dino in temp:
        pila.push(dino)
    return len(especies)

def contar_descubridores(pila):
    descubridores = {}
    temp = []
    while pila.size() > 0:
        dino = pila.pop()
        temp.append(dino)
        if dino['descubridor'] not in descubridores:
            descubridores[dino['descubridor']] = True
    for dino in temp:
        pila.push(dino)
    return len(descubridores)

def mostrar_dinosaurios_con_T(pila):
    dinos_con_T = []
    temp = []
    while pila.size() > 0:
        dino = pila.pop()
        temp.append(dino)
        if dino['nombre'].startswith('T'):
            dinos_con_T.append(dino['nombre'])
    for dino in temp:
        pila.push(dino)
    return dinos_con_T

def mostrar_dinosaurios_menos_275kg(pila):
    dinos_menos_275kg = []
    temp = []
    while pila.size() > 0:
        dino = pila.pop()
        temp.append(dino)
        peso = int(dino['peso'].replace(' kg', ''))
        if peso < 275:
            dinos_menos_275kg.append(dino['nombre'])
    for dino in temp:
        pila.push(dino)
    return dinos_menos_275kg

def separar_dinosaurios_AQS(pila):
    pila_AQS = Stack()
    temp = []
    while pila.size() > 0:
        dino = pila.pop()
        temp.append(dino)
        if dino['nombre'][0] in 'AQS':
            pila_AQS.push(dino)
    for dino in temp:
        pila.push(dino)
    return pila_AQS

print("Número de especies:", contar_especies(pila_dinosaurios))
print("Número de descubridores:", contar_descubridores(pila_dinosaurios))
print("Dinosaurios que empiezan con T:", mostrar_dinosaurios_con_T(pila_dinosaurios))
print("Dinosaurios que pesan menos de 275 kg:", mostrar_dinosaurios_menos_275kg(pila_dinosaurios))

pila_AQS = separar_dinosaurios_AQS(pila_dinosaurios)
dinos_AQS = []
while pila_AQS.size() > 0:
    dinos_AQS.append(pila_AQS.pop()['nombre'])
print("Dinosaurios que comienzan con A, Q, S:", dinos_AQS)