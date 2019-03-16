'''
operacje na napisach
'''

napis = 'Ala ma kota'

print(napis.replace('kota', 'psa'))

print(napis.upper())
print(napis.lower())
print(f'w zdaniu jest {napis.count("a")} liter "a"')
print(f"litera 'k' jest na {napis.find('k')+1} miejscu")
napis = 'Ala ma kota \n\n'
print(napis*5) #strip