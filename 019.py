import _utilities


@_utilities.benchmark
def solve():
    day_id = 1
    year = 1900
    day_in_month = 1
    month = 0
    months_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    count = 0
    while year < 2001:
        if day_in_month == 1 and day_id % 7 == 0 and year >= 1901:
            count += 1
        day_id += 1
        day_in_month += 1
        if day_in_month > months_days[month]:
            if month == 1 and year % 4 == 0 and (year % 400 == 0 or year % 100 != 0):
                day_id += 1
            day_in_month = 1
            month += 1
        if month >= 12:
            month = 0
            year += 1
    return count


if __name__ == '__main__':
    solve()
