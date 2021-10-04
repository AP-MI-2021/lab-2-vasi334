def prim(n):
    if n == 1:
        return False
    elif n == 2:
        return True

    for d in range(2, n):
        if n % d == 0:
            return False

    return True


def is_superprime(n):
    n = int(n[::-1])
    aux = n % 10

    while n != 0:
        if not prim(aux):
            return False
        n //= 10
        aux = aux * 10 + n % 10

    return True


def test_is_superprime():
    numar = input('Verifica daca un numar este superprim: ')
    print(is_superprime(numar))


test_is_superprime()
