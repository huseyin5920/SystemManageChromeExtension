import phonenumbers
from phonenumbers import geocoder

phone_number = phonenumbers.parse("+905538351846", "TR")

print(geocoder.description_for_number(phone_number, "en"))
