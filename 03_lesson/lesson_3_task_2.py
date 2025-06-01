from smartphone import Smartphone

catalog = []

smartphone1 = Smartphone("Samsung", "Galaxy S23", "+79123456789")
smartphone2 = Smartphone("Apple", "iPhone 14", "+79234567890")
smartphone3 = Smartphone("Xiaomi", "Redmi Note 12", "+79345678901")
smartphone4 = Smartphone("Google", "Pixel 7", "+79456789012")
smartphone5 = Smartphone("OnePlus", "11", "+79567890123")

catalog.append(smartphone1)
catalog.append(smartphone2)
catalog.append(smartphone3)
catalog.append(smartphone4)
catalog.append(smartphone5)

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model} {smartphone.phone_number}")
