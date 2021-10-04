def get_leap_years(start, end):
    ani_bisecti = []
    for i in range(start, end + 1):
        if i % 400 == 0 or i % 100 != 0 and i % 4 == 0:
            ani_bisecti.append(i)
    return ani_bisecti


def test_get_leap_years():
    assert get_leap_years(1, 10) == [4, 8]
    assert get_leap_years(2000, 2016) == [2000, 2004, 2008, 2012, 2016]

test_get_leap_years()