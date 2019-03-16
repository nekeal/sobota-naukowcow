'''
scalanie slownikow i list
'''

slownik_a = {'a':1, 'b':2, 'c':3}
slownik_b = {'d':4, 'b':8}

lista_a = [1,2,3]
lista_b = [2,3,4]

print({**slownik_a, **slownik_b})
print([*lista_a, *lista_b])