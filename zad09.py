'''
zliczanie wystapien elementu w tablicy/stringu, usuwanie danego elementu
'''


liczba_binarna = "1111010101011100001"

print(liczba_binarna.count('1'), liczba_binarna.count('0'), len(liczba_binarna))

liczba_binarna = liczba_binarna.replace("1", '')

print(liczba_binarna, len(liczba_binarna))