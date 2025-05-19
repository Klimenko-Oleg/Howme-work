def is_year_leap(year):
    if year % 4 == 0:
        return True
    else:
        return False


year_to_check = 2023
is_leap = is_year_leap(year_to_check)

print(f"год {year_to_check}: {is_leap}")

year_to_check = 2024
is_leap = is_year_leap(year_to_check)

print(f"год {year_to_check}: {is_leap}")
