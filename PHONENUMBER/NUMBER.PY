"""
# Program to convert input to
# phonenumber format

import phonenumbers

# Parsing String to Phone number
# Phone number format: (+Countrycode)xxxxxxxxxx
phoneNumber = phonenumbers.parse("+916353716421")

# This will print the phone number and
# it's basic details.
print(phoneNumber)
"""

"""
# Program to get timezone a phone number

import phonenumbers
from phonenumbers import timezone

# Parsing String to Phone number
phoneNumber = phonenumbers.parse("+916353716421")

# Pass the parsed phone number in below function
timeZone = timezone.time_zones_for_number(phoneNumber)

# It print the timezone of a phonenumber
print(timeZone)
"""

# Program to find carrier and region
# of a phone number
import phonenumbers
from phonenumbers import geocoder, carrier

# Parsing String to Phone number
phoneNumber = phonenumbers.parse("+916353716421")

# Getting carrier of a phone number
Carrier = carrier.name_for_number(phoneNumber, 'en')

# Getting region information
Region = geocoder.description_for_number(phoneNumber, 'en')

# Printing the carrier and region of a phone number
print(Carrier)
print(Region)
