"""
Gaseste ultimul numar prim mai mic decat un numar dat
"""

def get_largest_prime_below(n):
    numar_de_testat = n - 1
    numaram_divizorii = 0
    ok = True

    while ok:
        for divizor in range(2, numar_de_testat):
            if numar_de_testat % divizor == 0:
                numaram_divizorii += 1  # = numaram_divizorii = numaram_divizorii + 1

        if numaram_divizorii == 0:
            return numar_de_testat
        else:
            numar_de_testat = numar_de_testat - 1
            numaram_divizorii = 0


def test_get_largest_below():
    a = int(input('Dati un numar: '))
    print(get_largest_prime_below(a))


test_get_largest_below()