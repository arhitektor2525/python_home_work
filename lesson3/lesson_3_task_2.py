from smartphone import Smartphone
catalog = [
    Smartphone("Sony", "Experia", "+71111111111"),
    Smartphone("Samsung", "Galaxy A8", "+72222222222"),
    Smartphone("Xiaomi", "Redmi Note 10", "+73333333333"),
    Smartphone("Poco", "P40", "+74444444444"),
    Smartphone("Nokia", "3310", "+755555555555")
]
for phone in catalog:
    print(phone.get_info())