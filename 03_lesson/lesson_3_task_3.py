from mailing import Mailing
from address import Address


address_to = Address("123456", "Moscow", "Tverskaya", "10", "25")
address_from = Address("654321", "Saint Petersburg", "Nevsky", "20", "50")

mailing = Mailing(
    to_address=address_to,
    from_address=address_from,
    cost=500.00,
    track="ABCD123456789"
)

print(
    f"Отправление {mailing.track} из {mailing.from_address.postal_code}, "
    f"{mailing.from_address.city}, {mailing.from_address.street}, "
    f"{mailing.from_address.house} - {mailing.from_address.apartment} в "
    f"{mailing.to_address.postal_code}, {mailing.to_address.city}, "
    f"{mailing.to_address.street}, {mailing.to_address.house} - "
    f"{mailing.to_address.apartment}. Стоимость {mailing.cost} рублей."
)
