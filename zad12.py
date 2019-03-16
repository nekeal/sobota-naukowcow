'''
odwracanie list/napisow
'''



lista = [1,2,3,4,5]
napis = "12345"

print(list(reversed(lista)))
print(lista[::-1])
lista.reverse()
print(lista)
print(napis[::-1])
print("".join(reversed(napis)))



