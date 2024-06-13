def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def find_next_anniversary(year):
    while True:
        if is_leap_year(year):
            return year
        year += 1

def find_previous_anniversary(year):
    while True:
        if is_leap_year(year):
            return year
        year -= 1

def parse_date(date_string):
    day, month, year = map(int, date_string.split('/'))
    return day, month, year

# Given date
date_string = "04/11/1946"
day, month, year = parse_date(date_string)

# Check if it's a leap year
if is_leap_year(year):
    print(f"{year} is a leap year.")
    next_anniversary = find_next_anniversary(year + 1)
    print(f"The next anniversary will be in {next_anniversary}.")
else:
    print(f"{year} is not a leap year.")
    previous_anniversary = find_previous_anniversary(year - 1)
    print(f"The previous anniversary was in {previous_anniversary}.")
