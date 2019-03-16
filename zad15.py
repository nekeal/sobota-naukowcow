'''
zwracanie wielu wartosci przez funckje
'''

def statystyka(lista):
    return min(lista), max(lista), sum(lista)


lista = [i for i in range(1,11)]

minimum, maksimum, suma = statystyka(lista)

print(minimum, maksimum, suma)