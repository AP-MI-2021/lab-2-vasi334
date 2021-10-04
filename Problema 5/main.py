def is_palindrome(n):
    return n == n[::-1]


def test_is_palindrome():
    numar = input('Verifica daca un numar este palindrom: ')
    print(is_palindrome(numar))


test_is_palindrome()
