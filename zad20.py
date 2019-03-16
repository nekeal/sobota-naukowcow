'''
iteracja po wielu listach jednoczesnie
'''


lista_a = [1, 4, 7]
lista_b = [2, 5, 8]
lista_c = [3, 6, 9]

for a,b,c in zip(lista_a, lista_b, lista_c):
    print(a, b, c)
