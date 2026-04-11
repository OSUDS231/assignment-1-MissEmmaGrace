## Part (a)
distance = float(input("Enter the trip distance (miles): "))
speed = float(input("Enter the average speed (mph): "))
fuel = float(input("Enter the fuel efficiency (mpg): "))
price = float(input("Enter the gas price per gallon: "))

## Part (b)
drivingtime = round(distance/speed, 1)
gas = round(distance/fuel, 1)
fuelcost = round(gas*price, 1)

## Part (c)
print()
print(f'For a trip of {distance} miles at an average speed of {speed} mph, the driving time will be {drivingtime} hours.')
print()
print(f'Your car will use {gas} gallons of gas, and the total fuel cost will be ${fuelcost}.')

