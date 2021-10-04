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

    zile_intre_ani = ani_b + ani_normali + zile_anul_nasterii(anul_nasterii, luna_nasterii, ziua_nasterii) + zile_anul_actual(anul_actual, luna_actuala, ziua_actuala)

    return zile_intre_ani


def test_get_age_in_days():
    b = input('Introdu data nasterii in formatul DD/MM/YYYY, separata prin "/": ')
    print(get_age_in_days(b))


test_get_age_in_days()
