from address import Address
from mailing import Mailing

to_address = Address("123456", "Воркута", "Ленина", "10", "25")
from_address = Address("654321", "Кагалым", "Пушкина", "5", "10")

mailing = Mailing(to_address, from_address, 500, "TRACK123456")

print(f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, {mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, {mailing.to_address.house} - {mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")