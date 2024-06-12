from Jedi import jedis
from lista import search, show_list, by_name, by_species

def listado_ordenado(jedis):
    jedis_ordenados_nombre = sorted(jedis, key=by_name)
    jedis_ordenados_especie = sorted(jedis, key=by_species)
    return jedis_ordenados_nombre, jedis_ordenados_especie

def mostrar_info(jedis, nombres):
    info_jedis = []
    for nombre in nombres:
        index = search(jedis, 'name', nombre)
        if index is not None:
            info_jedis.append(jedis[index])
    return info_jedis

def padawans_de_maestros(jedis, maestros):
    padawans = []
    for jedi in jedis:
        if jedi['master'] is not None:
            for maestro in maestros:
                if maestro in jedi['master']:
                    padawans.append(jedi['name'])
    return padawans

def jedis_por_especie(jedis, especies):
    jedis_especies = []
    for jedi in jedis:
        if jedi['species'] in especies:
            jedis_especies.append(jedi)
    return jedis_especies

def jedis_comienzan_con_a(jedis):
    jedis_a = []
    for jedi in jedis:
        if jedi['name'].startswith('A'):
            jedis_a.append(jedi)
    return jedis_a

def jedis_mas_de_un_color(jedis):
    jedis_multicolor = []
    for jedi in jedis:
        lightsaber_color = jedi['lightsaber_color']
        if lightsaber_color is not None and '/' in lightsaber_color:
            jedis_multicolor.append(jedi)
    return jedis_multicolor

def jedis_sable_amarillo_violeta(jedis):
    jedis_amarillo_violeta = []
    for jedi in jedis:
        lightsaber_color = jedi['lightsaber_color']
        if lightsaber_color is not None and ('Yellow' in lightsaber_color or 'Purple' in lightsaber_color):
            jedis_amarillo_violeta.append(jedi)
    return jedis_amarillo_violeta

def padawans_de_quigon_mace(jedis):
    padawans = []
    for jedi in jedis:
        if jedi['master'] is not None:
            if 'Qui-Gon Jinn' in jedi['master'] or 'Mace Windu' in jedi['master']:
                padawans.append(jedi['name'])
    return padawans

def jedis_grand_master(jedis):
    grand_masters = []
    for jedi in jedis:
        if 'Grand Master' in jedi['rank']:
            grand_masters.append(jedi)
    return grand_masters

jedis_ordenados_nombre, jedis_ordenados_especie = listado_ordenado(jedis)
show_list('Listado de Jedi ordenado por nombre:', jedis_ordenados_nombre)
show_list('Listado de Jedi ordenado por especie:', jedis_ordenados_especie)

info_jedis = mostrar_info(jedis, ['Ahsoka Tano', 'Kit Fisto'])
show_list('Información de Ahsoka Tano y Kit Fisto:', info_jedis)

padawans = padawans_de_maestros(jedis, ['Yoda', 'Luke Skywalker'])
show_list('Padawans de Yoda y Luke Skywalker:', padawans)

jedis_humanos_twilek = jedis_por_especie(jedis, ['Human', "Twi'lek"])
show_list("Jedi de especie humana y twi'lek:", jedis_humanos_twilek)

jedis_a = jedis_comienzan_con_a(jedis)
show_list('Jedi que comienzan con A:', jedis_a)

jedis_multicolor = jedis_mas_de_un_color(jedis)
show_list('Jedi que usaron sable de luz de más de un color:', jedis_multicolor)

jedis_amarillo_violeta = jedis_sable_amarillo_violeta(jedis)
show_list('Jedi que utilizaron sable de luz amarillo o violeta:', jedis_amarillo_violeta)

padawans_quigon_mace = padawans_de_quigon_mace(jedis)
show_list('Padawans de Qui-Gon Jinn y Mace Windu:', padawans_quigon_mace)

grand_masters = jedis_grand_master(jedis)
show_list('Jedi con el ranking de Grand Master:', grand_masters)