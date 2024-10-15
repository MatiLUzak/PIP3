import math


def sito(limit):
    nie_pierwsze=set()
    for i in range(2,int(math.sqrt(limit))+1):
        if i not in nie_pierwsze:
            for j in range(i*i,limit+1,i):
                nie_pierwsze.add(j)
    return [i for i in range(2,limit+1) if i not in nie_pierwsze]


def rozklad(n):
    slownik_czynniki = {}

    while n % 2 == 0:
        if 2 in slownik_czynniki:
            slownik_czynniki[2] += 1
        else:
            slownik_czynniki[2] = 1
        n = n // 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            if i in slownik_czynniki:
                slownik_czynniki[i] += 1
            else:
                slownik_czynniki[i] = 1
            n = n // i

    if n > 2:
        slownik_czynniki[n] = 1

    return slownik_czynniki


def nwm(a, b):
    czynniki_a = rozklad(a)
    czynniki_b = rozklad(b)

    wszystkie_czynniki = set(czynniki_a.keys()).union(set(czynniki_b.keys()))

    lcm = 1
    for czynnik in wszystkie_czynniki:
        potega_a = czynniki_a.get(czynnik, 0)
        potega_b = czynniki_b.get(czynnik, 0)
        lcm *= czynnik ** max(potega_a, potega_b)

    return lcm

if __name__ == '__main__':
    pierwsze=sito(100)
    print(pierwsze)
    print(nwm(192, 348))