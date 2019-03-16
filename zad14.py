'''
enumerate
'''


lista = ['a', 'b', 'c', 'd', 'e']

for element in lista:
    print(element)

print('---')

for i, element in enumerate(lista):
    print(i, element)

print('----')

for i, element in enumerate(lista):
    print(i, lista[i])
