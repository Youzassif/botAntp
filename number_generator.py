import random

def generator(size):
    number = []
    for i in range(size):
        n = random.randint(111111111,999999999)
        number.append('0'+str(n))
    return number