import phonenumbers
from test import number


from phonenumbers import geocoder

coutry_number=phonenumbers.parse(number,"CH")
print(geocoder.description_for_number(coutry_number,"en"))


from phonenumbers import carrier
service_numner=phonenumbers.parse(number,"RO")
print(carrier.name_for_number(service_numner,"en"))
