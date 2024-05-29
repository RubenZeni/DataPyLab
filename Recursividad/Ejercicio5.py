'''Desarrollar una función que permita convertir un número romano en un número decimal.'''
def romano_a_decimal(romano):
    valores = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if len(romano) == 0:
        return 0
    if len(romano) == 1:
        return valores[romano]
    if valores[romano[0]] < valores[romano[1]]:
        return -valores[romano[0]] + romano_a_decimal(romano[1:])
    else:
        return valores[romano[0]] + romano_a_decimal(romano[1:])
    
print(f'Número en decimal: {romano_a_decimal(input('Ingrese un número romano: '))}')