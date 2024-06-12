def listar_lista_inversa(lista):
    if len(lista) <= 1:
        return lista
    else:
        return listar_lista_inversa(lista[1:]) + [lista[0]]

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f'Lista original: {lista}')
print(f'Lista invertida: {listar_lista_inversa(lista)}')