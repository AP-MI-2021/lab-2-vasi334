"""
Problema 1
"""


def get_largest_prime_below(n):
    if n <= 2:
        return None

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
    assert get_largest_prime_below(50) == 47
    assert get_largest_prime_below(100) == 97
    assert get_largest_prime_below(20) == 19
    assert get_largest_prime_below(60) == 59


"""
Problema 2
"""

from datetime import date

today = date.today()

# dd/mm/YY
d1 = today.strftime("%d/%m/%Y")
lista_1 = d1.split('/')


def ani_bisecti(an_1, an_2):
    count = 0
    for i in range(an_1 + 1, an_2):
        if i % 400 == 0 or i % 100 != 0 and i % 4 == 0:
            count += 1
    return count


def zile_anul_nasterii(anul_nasterii, luna_nasterii, ziua_nasterii):
    zile_in_primul_an = 0

    for i in range(luna_nasterii, 12 + 1):
        if i == 2:
            zile_in_primul_an += 28
        elif i % 2 != 0 or i % 8 == 0:
            zile_in_primul_an += 31
        else:
            zile_in_primul_an += 30

    if anul_nasterii % 400 == 0 or anul_nasterii % 100 != 0 and anul_nasterii % 4 == 0:
        zile_in_primul_an += 1

    return zile_in_primul_an - ziua_nasterii


def zile_anul_actual(anul_actual, luna_actuala, ziua_actuala):
    zile_in_anul_actual = 0

    for i in range(1, luna_actuala):
        if i == 2:
            zile_in_anul_actual += 28
        elif i % 2 != 0 or i % 8 == 0:
            zile_in_anul_actual += 31
        else:
            zile_in_anul_actual += 30

    if anul_actual % 400 == 0 or anul_actual % 100 != 0 and anul_actual % 4 == 0:
        zile_in_anul_actual += 1

    return zile_in_anul_actual + ziua_actuala


def get_age_in_days(birthday):
    lista = birthday.split('/')

    ziua_nasterii = int(lista[0])
    luna_nasterii = int(lista[1])
    anul_nasterii = int(lista[2])

    ziua_actuala = int(lista_1[0])
    luna_actuala = int(lista_1[1])
    anul_actual = int(lista_1[2])

    ani_b = ani_bisecti(anul_nasterii, anul_actual) * 366
    ani_normali = (anul_actual - anul_nasterii - ani_bisecti(anul_nasterii, anul_actual) - 1) * 365

    zile_intre_ani = ani_b + ani_normali + zile_anul_nasterii(anul_nasterii, luna_nasterii,
                                                              ziua_nasterii) + zile_anul_actual(anul_actual,
                                                                                                luna_actuala,
                                                                                                ziua_actuala)

    return zile_intre_ani


def test_get_age_in_days():
    assert get_age_in_days('22/11/2001') == 7257
    assert get_age_in_days('12/01/2002') == 7206
    assert get_age_in_days('23/06/1969') == 19097


"""
Problema 3
"""


def get_leap_years(start, end):
    ani_bisecti = []
    for i in range(start, end + 1):
        if i % 4 == 0:
            if i % 100 == 0 or i % 400 == 0:
                ani_bisecti.append(i)
    return ani_bisecti


def test_get_leap_years():
    assert get_leap_years(1, 10) == [4, 8]
    assert get_leap_years(2000, 2016) == [2000, 2004, 2008, 2012, 2016]
    assert get_leap_years(1882, 1906) == [1884, 1888, 1892, 1896, 1904]


def main():
    a = input("""
    Alegeti:
    1. Pentru a gasi cel mai mare numar prim sub un numar
    2. Pentru a afla ziua nasterii in zile
    3. Pentru a afla anii bisecti intr-o perioada
    4. Pentru a iesi 
    """)
    while a != '4':
        if a == '1':
            test_get_largest_below()
        elif a == '2':
            test_get_age_in_days()
        elif a == '3':
            test_get_leap_years()


if __name__ == '__main__':
    main()
