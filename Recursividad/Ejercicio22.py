'''El problema de la mochila Jedi. Suponga que un Jedi (Luke Skywalker, Obi-Wan Kenobi, Rey u otro, el que más le guste) está atrapado, pero muy cerca está su mochila que contiene muchos objetos. Implementar una función recursiva llamada “usar la fuerza” que le permita al Jedi “con ayuda de la fuerza” realizar las siguientes actividades:
a. sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no queden más objetos en la mochila;
b. determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sacar para encontrarlo;
c. Utilizar un vector para representar la mochila.'''
def usar_la_fuerza(mochila):
    if not mochila:
        return ("No quedan objetos en la mochila.")
    objeto = mochila.pop()
    if objeto == "sable de luz":
        return (f"Encontraste el sable de luz. Fue necesario sacar {len(mochila)} objetos para lograrlo.")
    else:
        return usar_la_fuerza(mochila)
    
mochila = ["esfera de la paz", "anillos de vaale", "mapa estelar", "guía del contrabandista", "sable de luz", "cristal nova", "infante de shaa"]
print(usar_la_fuerza(mochila))