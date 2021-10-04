def is_antipalindrome(n):
    i = 0
    k = len(n) - 1
    ok = True

    while i < k and ok:
        if n[i] != n[k]:
            ok = False
        i += 1
        k -= 1

    return ok


def test_is_antipalindrome():
    nr = input('Verifica daca un numar este antipalindrom: ')
    print(is_antipalindrome(nr))


test_is_antipalindrome()
