'''
args i kwargs
'''

def funkcja(*args, **kwargs):
    print(args)
    print(kwargs)


funkcja(1,2,3,4, a=1, b=2, c=3)