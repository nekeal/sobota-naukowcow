from pprint import pprint

'''
ladne printowanie - pretty print :)
'''

plansza = [[j for j in range(1,9)] for i in range(1,9)]

print(plansza,end="\n\n")

pprint(plansza)

print("\n")
input()
slownik = {i:i**2 for i in range(2,100)}

pprint(slownik)