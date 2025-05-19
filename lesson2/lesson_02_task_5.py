def month_to_season(month_number):
    seasons = {
        1: "Зима", 2: "Зима", 12: "Зима",
        3: "Весна", 4: "Весна", 5: "Весна",
        6: "Лето", 7: "Лето", 8: "Лето",
        9: "Осень", 10: "Осень", 11: "Осень"
    }
    return seasons.get(month_number, "Некорректный номер месяца")


print(month_to_season(2))
print(month_to_season(4))
print(month_to_season(7))
print(month_to_season(10))
print(month_to_season(13))
