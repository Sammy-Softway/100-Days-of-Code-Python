import requests
from datetime import datetime as dt

MY_LAT = 6.5244
MY_LONG = 3.3792

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response)
# response.raise_for_status()
#
# data = response.json()
# print(data)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get(url='https://api.sunrise-sunset.org/v2', params=parameters)
response.raise_for_status()

data = response.json()
sunrise = data['sunrise']
sunset = data['sunset']
print(data)
print(sunrise)
print(sunset)

time_now = dt.now()
print(time_now)

print(sunrise.split('T'))
print(sunset.split('T'))

print(sunrise.split('T')[1].split(':'))
print(sunset.split('T')[1].split(':'))

print(sunrise.split('T')[1].split(':')[0])
print(sunset.split('T')[1].split(':')[0])
print(time_now.hour)