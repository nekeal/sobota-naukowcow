'''
usuwanie zagniezdzen w listach
'''
import itertools
import more_itertools

lista_a = [[1,2],[3,4],[5,6]]

lista_b = [1,2,3, [4,5, [6,7, [8,9]]]]

print(list(itertools.chain.from_iterable(lista_a)))

print(list(more_itertools.collapse(lista_b)))