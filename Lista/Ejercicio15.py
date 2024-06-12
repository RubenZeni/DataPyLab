from random import randint

# Datos de ejemplo
entrenadores = [
{
    'nombre': 'Ash Ketchum',
    'torneos_ganados': 7,
    'batallas_perdidas': 50,
    'batallas_ganadas': 120
},
{
    'nombre': 'Goh',
    'torneos_ganados': 2,
    'batallas_perdidas': 10,
    'batallas_ganadas': 40
},
{
    'nombre': 'Leon',
    'torneos_ganados': 10,
    'batallas_perdidas': 5,
    'batallas_ganadas': 100
},
{
    'nombre': 'Chloe',
    'torneos_ganados': 1,
    'batallas_perdidas': 8,
    'batallas_ganadas': 30
},
{
    'nombre': 'Raihan',
    'torneos_ganados': 4,
    'batallas_perdidas': 15,
    'batallas_ganadas': 60
}
]

pokemons = [
{
    'nombre': 'Pikachu',
    'nivel': 35,
    'tipo': 'Eléctrico',
    'subtipo': None
},
{
    'nombre': 'Charizard',
    'nivel': 40,
    'tipo': 'Fuego',
    'subtipo': 'Volador'
},
{
    'nombre': 'Bulbasaur',
    'nivel': 30,
    'tipo': 'Planta',
    'subtipo': 'Veneno'
},
{
    'nombre': 'Starmie',
    'nivel': 30,
    'tipo': 'Agua',
    'subtipo': 'Psíquico'
},
{
    'nombre': 'Psyduck',
    'nivel': 25,
    'tipo': 'Agua',
    'subtipo': None
},
{
    'nombre': 'Gyarados',
    'nivel': 35,
    'tipo': 'Agua',
    'subtipo': 'Volador'
},
{
    'nombre': 'Onix',
    'nivel': 38,
    'tipo': 'Roca',
    'subtipo': 'Tierra'
},
{
    'nombre': 'Geodude',
    'nivel': 28,
    'tipo': 'Roca',
    'subtipo': 'Tierra'
},
{
    'nombre': 'Vulpix',
    'nivel': 20,
    'tipo': 'Fuego',
    'subtipo': None
},
{
    'nombre': 'Blastoise',
    'nivel': 50,
    'tipo': 'Agua',
    'subtipo': None
},
{
    'nombre': 'Umbreon',
    'nivel': 45,
    'tipo': 'Siniestro',
    'subtipo': None
},
{
    'nombre': 'Nidoking',
    'nivel': 40,
    'tipo': 'Veneno',
    'subtipo': 'Tierra'
}
]

for entrenador in entrenadores:
    entrenador.update({'pokemons': []})
    for i in range(randint(1, 5)):
        entrenador['pokemons'].append(pokemons[randint(0, len(pokemons) - 1)])

