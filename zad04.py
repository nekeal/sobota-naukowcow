'''
jednolinijkowa petla for
'''
from pprint import pprint

lista = [i**2 for i in range(2, 100)]

print(lista)

slownik = {i:i**2 for i in range(2,100)}

pprint(slownik)